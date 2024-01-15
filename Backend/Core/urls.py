
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Core.views import imprimir,index,robots,categoria,desenho,about,ads


app_name = 'Core'

urlpatterns = [
    path('',view=index,name='index'),
    path('categoria/<int:id>',view=categoria,name='categoria'),
    path('desenho/<int:id>',view=desenho,name='desenho'),
    path('about/',view=about,name='about'),
    path('imprimir/<int:id>',view=imprimir, name='imprimir'),
    path('ads.txt',ads),
    path('robots.txt',robots),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)