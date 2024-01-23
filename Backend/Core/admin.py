from django.contrib import admin
from .models import Imagem,Categoria,Contato



@admin.register(Imagem)
class ImagenAdmin(admin.ModelAdmin):
    list_display =('icone','nome','categoria','descricao','data_upload')
    list_filter =('categoria','data_upload')



admin.site.register(Categoria)

@admin.action(description="Marcar como Lido")
def action_read_messenger(modeladmin,request,queryset):
    for mensagem in queryset:
        mensagem.Lido = True
        mensagem.save()

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('Nome','Email','Telefone','Mensagem','Lido')
    readonly_fields=('Nome','Email','Telefone','Mensagem')
    list_filter = ('Lido',)
    actions = [action_read_messenger,]