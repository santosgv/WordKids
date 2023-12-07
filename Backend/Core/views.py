from django.shortcuts import render
from .models import Imagem
from .serializers import ImagemSerializer,CategoriaSerializer
from rest_framework import viewsets,status


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = CategoriaSerializer