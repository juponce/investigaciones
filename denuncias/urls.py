from django.urls import path
from .views import *

urlpatterns = [
    path('', denuncias, name='denuncias'),
    path('audioTexto/', audioTexto, name='audioTexto'),
]