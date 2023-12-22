from django.contrib import admin
from .models import Imagem,Categoria



@admin.register(Imagem)
class ImagenAdmin(admin.ModelAdmin):
    list_display =('nome','categoria','icone','descricao','data_upload')
    list_filter =('categoria','data_upload')



admin.site.register(Categoria)