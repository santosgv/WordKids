from .models import Imagem,Categoria,Contato
from django.shortcuts import  render,redirect,get_object_or_404
from django.core.paginator import Paginator
import os
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.db.models import Count
from .tasks import tastk_imprimir

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
        return redirect("/contact/?status=1")

@cache_page(60 * 100)
def politica(request):
     categorias = get_categorias_com_contagem()
     return render(request,'politica-de-privacidade.html',{'categorias':categorias,})

@cache_page(60 * 100)
def transparencia(request):
     categorias = get_categorias_com_contagem()
     return render(request,'transparencia.html',{'categorias':categorias,})

def imprimir(request,id):
    tastk_imprimir.delay(id)
    return None


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

@cache_page(60 * 100) 
def sitemap(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT,'sitemap.xml')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='application/xml')
    else:
        path = os.path.join(settings.BASE_DIR,'templates/static/sitemap.xml')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='application/xml')