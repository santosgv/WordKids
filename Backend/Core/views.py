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


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(detail=True, methods=['get'])
    def categoria_desenho(self, request, pk=None):
        try:
            categoria = self.get_object()
            desenhos = categoria.imagem_set.all()  # Use 'imagem_set' para acessar os desenhos associados à categoria
            serializer = ImagemSerializer(desenhos, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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