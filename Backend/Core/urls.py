
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Core.views import imprimir,index,robots,categoria,desenho,about,politica,ads,transparencia,contact


app_name = 'Core'

urlpatterns = [
    path('',view=index,name='index'),
    path('categoria/<str:nome>',view=categoria,name='categoria'),
    path('desenho/<str:nome>',view=desenho,name='desenho'),
    path('about/',view=about,name='about'),
    path('politica/',view=politica,name='politica'),
    path('transparencia/',view=transparencia,name='transparencia'),
    path("contact/", view=contact, name='contact'),
    path('imprimir/<int:id>',view=imprimir, name='imprimir'),
    path('ads.txt',ads),
    path('robots.txt',robots),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)