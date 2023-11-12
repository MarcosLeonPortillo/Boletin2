from django.urls import path
from Boletin2 import views

urlpatterns = [
    
    path('', views.crea_formulario, name='crea_formulario'),
    

]
