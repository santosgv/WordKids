
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Core.views import robots,imprimir


app_name = 'Core'

urlpatterns = [
    path('imprimir/<int:id>',imprimir, name='imprimir'),
    path('robots.txt',robots),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)