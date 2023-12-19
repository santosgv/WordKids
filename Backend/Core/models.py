from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Imagem(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria,null=True, blank=True, on_delete=models.DO_NOTHING)
    arquivo = models.ImageField(upload_to='Imagens')
    descricao = models.TextField(blank=True)
    data_upload = models.DateTimeField(auto_now_add=True)
    afiliado= RichTextField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.nome