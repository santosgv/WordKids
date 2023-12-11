from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Core.views import ImagemViewSet,CategoriaViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'imagens', ImagemViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',include('Core.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)