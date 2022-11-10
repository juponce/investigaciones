from django.shortcuts import render

# Create your views here.

def rutas(request):
    return render(request, 'rutasHorarios/rutas.html')