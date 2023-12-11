from django.http import FileResponse
from django.shortcuts import render
from .models import Imagem
from .serializers import ImagemSerializer,CategoriaSerializer
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import os
from django.conf import settings
from rest_framework import viewsets,status


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = CategoriaSerializer

def imprimir(request,id):
        try:
            image = Imagem.objects.get(id=id)
            buffer = io.BytesIO()
            PDF = canvas.Canvas(buffer,pagesize=letter)
            PDF.drawImage(os.path.join(settings.BASE_DIR, 'media',f'{image.arquivo}'),0, 0, width=letter[0], height=letter[1])
            PDF.showPage()
            PDF.save()
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename='Mundo Colorido Kids - Desenho.pdf')
        except Exception as msg:
            print(msg)