import datetime
from .models import Imagem,Categoria,Contato,Email
from django.contrib.auth.decorators import login_required
from .utils import email_html
from django.shortcuts import  render,redirect,get_object_or_404
from django.core.paginator import Paginator
import os
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.db.models import Count
from django.contrib import sitemaps
from PIL import Image
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import FileResponse,JsonResponse
from django.contrib import messages
from django.contrib.messages import constants
import logging

logger = logging.getLogger('MyApp')

def get_categorias_com_contagem():
    cached_categorias = cache.get('all_categorias_com_contagem')
    if cached_categorias is None:
        categorias = Categoria.objects.annotate(quantidade=Count('imagem')).values('id', 'nome', 'quantidade')
        cached_categorias = [{'id': cat['id'], 'nome': cat['nome'], 'quantidade': cat['quantidade']} for cat in categorias]
        cache.set('all_categorias_com_contagem', cached_categorias, timeout=1800)
    return cached_categorias

def index(request):
     categorias = get_categorias_com_contagem()
     imagens = Imagem.objects.only('nome','arquivo','descricao').filter(destaque=True).all().order_by('-id')
     pagina = Paginator(imagens,25)
     pg_number = request.GET.get('page')
     imgs = pagina.get_page(pg_number)
     return render(request,'index.html',{'imagens':imgs,'categorias':categorias,})

def categoria(request,nome):
     categoria_nome = get_object_or_404(Categoria, nome=nome)
     categorias = get_categorias_com_contagem()
     imagens = Imagem.objects.only('nome','arquivo','descricao').filter(categoria=categoria_nome).order_by('-id')
     pagina = Paginator(imagens,25)
     pg_number = request.GET.get('page')
     imgs = pagina.get_page(pg_number)
     return render(request,'categoria.html',{'imagens':imgs,'categorias':categorias,})

def desenho(request,nome):
     categorias = get_categorias_com_contagem()
     img = Imagem.objects.filter(nome=nome)
     return render(request,'desenho.html',{'img':img,'categorias':categorias,})


def add_to_favorito(request, item):
    favoritos = request.session.get('favoritos', [])
    favoritos.append(item)
    request.session['favoritos'] = favoritos
    return HttpResponse(status=204)

def remove_from_favorito(request, item):
    favoritos = request.session.get('favoritos', [])
    if item in favoritos:
        favoritos.remove(item)
        request.session['favoritos'] = favoritos
        return redirect('/favoritos')
    else:
        return JsonResponse({'error': 'Item não encontrado nos favoritos'}, status=404)

def favoritos(request):
    categorias = get_categorias_com_contagem()
    favoritos = request.session.get('favoritos', [])
    request.session['favoritos'] = favoritos
    return render(request, 'favoritos.html', {'categorias':categorias,'favoritos': favoritos})

@cache_page(60 * 100)
def about(request):
     categorias = get_categorias_com_contagem()
     return render(request,'about.html',{'categorias':categorias,})

def contact(request):
    if request.method == "GET":
        categorias = get_categorias_com_contagem()
        status = request.GET.get('status')
        return render(request,'contact.html',{'status':status,'categorias':categorias})
    else:
        NOME = request.POST.get('name')
        EMAIL = request.POST.get('email')
        TELEFONE = request.POST.get('phone')
        MENSAGEM = request.POST.get('message')
        
        new_contato= Contato(
            Nome=NOME,
            Email=EMAIL,
            Telefone=TELEFONE,
            Mensagem=MENSAGEM
        )
        new_contato.save()
        messages.add_message(request, constants.SUCCESS, 'Enviado com sucesso')
        return redirect("/")

@cache_page(60 * 100)
def politica(request):
     categorias = get_categorias_com_contagem()
     return render(request,'politica-de-privacidade.html',{'categorias':categorias,})

@cache_page(60 * 100)
def transparencia(request):
     categorias = get_categorias_com_contagem()
     return render(request,'transparencia.html',{'categorias':categorias,})

def imprimir(request,id):
        try:
            image = Imagem.objects.get(id=id)
            buffer = io.BytesIO()
            PDF = canvas.Canvas(buffer, pagesize=letter)

            # Abre a imagem usando PIL
            img_path = os.path.join(settings.BASE_DIR, 'media', f'{image.arquivo}')
            img = Image.open(img_path)

            # Converte a imagem para preto e branco
            img = img.convert("L")

            # Obtém as dimensões da folha A4
            a4_width, a4_height = letter

            # Calcula as proporções para manter a escala
            width_ratio = a4_width / img.width
            height_ratio = a4_height / img.height
            min_ratio = min(width_ratio, height_ratio)

            # Calcula as novas dimensões da imagem mantendo a escala
            new_width = int(img.width * min_ratio)
            new_height = int(img.height * min_ratio)

            # Calcula as coordenadas para centralizar a imagem na folha
            x_offset = (a4_width - new_width) / 2
            y_offset = (a4_height - new_height) / 2

            # Desenha a imagem na folha A4 mantendo a escala
            PDF.drawInlineImage(img, x_offset, y_offset, width=new_width, height=new_height)
            PDF.drawString(120,2,'Visite https://mundocoloridokids.com.br para mais desenhos')

            PDF.showPage()
            PDF.save()

            buffer.seek(0)
            response = FileResponse(buffer, as_attachment=True, filename='Mundo Colorido Kids - Desenho.pdf')
            response.status_code = 200
            return response
        except Exception as msg:
            response = msg


@cache_page(60 * 100)
def robots(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT,'robots.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')
    else:
        path = os.path.join(settings.BASE_DIR,'templates/static/robots.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')

@cache_page(60 * 100)
def ads(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT,'ads.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')
    else:
        path = os.path.join(settings.BASE_DIR,'templates/static/ads.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')


def formulario(request):
    if request.method =="POST":
        email = request.POST.get('email')
        valida = Email.objects.filter(email=email)
        if valida.exists():
            messages.add_message(request, constants.ERROR, 'Email Ja cadastrado')
            logger.info(f'Email Ja cadastrado {email} '+str(datetime.datetime.now())+' horas!')
            return redirect("/")
        cadastrar = Email.objects.create(
            email=email
        )
        cadastrar.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastrado com sucesso')
        return redirect("/")
    
def unsubscriber(request,id):
    email = Email.objects.get(id=id)
    email.ativo =False
    email.save()
    return HttpResponse('Cancelado sua Inscriçao')

@login_required(login_url='/admin/login/?next=/admin/') 
def enviar_emeil(request):
    try:
        path_template = os.path.join(settings.BASE_DIR, 'Core/templates/emails/email.html')
        base_url = request.build_absolute_uri('/')
        emails = Email.objects.filter(ativo=True).all()
        posts = Imagem.objects.only('nome','descricao').filter(destaque=True).all().order_by('-id')[:15]

        for email in emails:
            email_html(path_template, 'Novos Desenhos', [email,],posts=posts,email=email,base_url=base_url)
            messages.add_message(request, constants.SUCCESS, 'Emais enviados com sucesso')
            return redirect("/")
        
    except Exception as msg:
        messages.add_message(request, constants.ERROR, f'Nao foi possivel enviar os Emails consulte o arquivo de Log')
        logger.critical(f'{msg} '+str(datetime.datetime.now())+' horas!')
        return redirect("/")

 
class Sitemap(sitemaps.Sitemap):
    i18n = True
    changefreq ='monthly'
    priority = 0.7

    def items(self):
        return Imagem.objects.all()        

    def lastmod(self, obj):
        return obj.data_upload