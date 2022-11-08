from django.shortcuts import render

# Create your views here.

def geo(request):
    return render(request, 'geolocalizacion/geo.html')