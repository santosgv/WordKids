from django.http import FileResponse
from .models import Imagem,Categoria,Contato
from django.shortcuts import  render,redirect
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.core.paginator import Paginator
import io
import os
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from PIL import Image


def get_categorias():
    cached_categorias = cache.get('all_categorias')
    if cached_categorias is None:
        categorias = Categoria.objects.values('id', 'nome')
        cached_categorias = [{'id': cat['id'], 'nome': cat['nome']} for cat in categorias]
        cache.set('all_categorias', cached_categorias, timeout=1800)
    return cached_categorias


def index(request):
     categorias = get_categorias()
     imagens = Imagem.objects.only('nome','arquivo','descricao').filter(destaque=True).all().order_by('-id')
     pagina = Paginator(imagens,25)
     pg_number = request.GET.get('page')
     imgs = pagina.get_page(pg_number)
     return render(request,'index.html',{'imagens':imgs,'categorias':categorias,})

def categoria(request,nome):
     categorias = get_categorias()
     imagens = Imagem.objects.only('nome','arquivo','descricao').filter(categoria=nome).order_by('-id')
     pagina = Paginator(imagens,25)
     pg_number = request.GET.get('page')
     imgs = pagina.get_page(pg_number)
     return render(request,'categoria.html',{'imagens':imgs,'categorias':categorias,})

def desenho(request,nome):
     categorias = get_categorias()
     img = Imagem.objects.filter(nome=nome)
     return render(request,'desenho.html',{'img':img,'categorias':categorias,})

@cache_page(60 * 15)
def about(request):
     categorias = get_categorias()
     return render(request,'about.html',{'categorias':categorias,})

def contact(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render(request,'contact.html',{'status':status})
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
        return redirect("/contact/?status=1")


def politica(request):
     categorias = get_categorias()
     return render(request,'politica-de-privacidade.html',{'categorias':categorias,})

def transparencia(request):
     categorias = get_categorias()
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

            PDF.showPage()
            PDF.save()

            buffer.seek(0)
            response = FileResponse(buffer, as_attachment=True, filename='Mundo Colorido Kids - Desenho.pdf')
            response.status_code = 200
            return response
        except Exception as msg:
            response = msg
            response.status_code = 404
            return JsonResponse({"error": str(msg)}, status=response.status_code)


def robots(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT,'robots.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')
    else:
        path = os.path.join(settings.BASE_DIR,'templates/static/robots.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')

@cache_page(60 * 15)
def ads(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT,'ads.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')
    else:
        path = os.path.join(settings.BASE_DIR,'templates/static/ads.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')