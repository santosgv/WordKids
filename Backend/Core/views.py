from django.http import FileResponse
from rest_framework.response import Response
from .models import Imagem,Categoria
from .serializers import ImagemSerializer,CategoriaSerializer
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import os
from django.conf import settings
from rest_framework import viewsets,status,pagination
from rest_framework.decorators import action
from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from PIL import Image



class CustomPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all().order_by('id')
    serializer_class = ImagemSerializer
    pagination_class = CustomPagination 


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('id')
    serializer_class = CategoriaSerializer


    @action(detail=True, methods=['get'])
    def categoria_desenho(self, request, pk=None):
        try:
            categoria = self.get_object()
            desenhos = categoria.imagem_set.all().order_by('id')
            paginator = CustomPagination()
            result_page = paginator.paginate_queryset(desenhos, request)
            serializer = ImagemSerializer(result_page, many=True, context={'request': request})
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

@cache_page(60 * 15)
def robots(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT,'robots.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')
    else:
        path = os.path.join(settings.BASE_DIR,'templates/static/robots.txt')
        with open(path,'r') as arq:
            return HttpResponse(arq, content_type='text/plain')