
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Core import views


app_name = 'Core'
urlpatterns = [
    path('imprimir/<int:id>',views.imprimir, name='imprimir'),

]
