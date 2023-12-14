from rest_framework import serializers
from Core.models import Imagem,Categoria

class ImagemSerializer(serializers.ModelSerializer):


    class Meta:
        model = Imagem
        fields = '__all__'



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'