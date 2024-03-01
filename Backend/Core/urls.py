
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from Core.views import imprimir,index,robots,categoria,desenho,add_to_favorito,favoritos,about,politica,ads,transparencia,contact,remove_from_favorito,formulario,unsubscriber,enviar_emeil,Sitemap


app_name = 'Core'

sitemaps = {
    'sitemap': Sitemap,
}

urlpatterns = [
    path('',view=index,name='index'),
    path('categoria/<str:nome>',view=categoria,name='categoria'),
    path('desenho/<str:nome>',view=desenho,name='desenho'),
    path('add_to_favorito/<item>', view=add_to_favorito, name='add_to_favorito'),
    path('remove_from_favorito/<item>', view=remove_from_favorito, name='remove_from_favorito'),
    path('favoritos/',view=favoritos,name='favoritos'),
    path('about/',view=about,name='about'),
    path('politica/',view=politica,name='politica'),
    path('transparencia/',view=transparencia,name='transparencia'),
    path("contact/", view=contact, name='contact'),
    path('imprimir/<int:id>',view=imprimir, name='imprimir'),
    path('ads.txt',ads),
    path('enviar_emeil/',view=enviar_emeil, name='enviar_emeil'),
    path("formulario/", view=formulario, name='formulario'),
    path('unsubscriber/<int:id>',view=unsubscriber, name='unsubscriber'),
    path('sitemap.xml',sitemap, {'sitemaps': sitemaps}),
    path('robots.txt',robots),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)