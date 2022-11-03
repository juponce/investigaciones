from django.urls import path
from .views import *

urlpatterns = [
    path('', informe, name='informes'),
    path('informe_pdf', informeGen, name='informe_pdf'),
]