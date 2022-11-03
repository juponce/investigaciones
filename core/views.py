from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
class HomeView(LoginView):
    template_name = 'core/index.html'

def home(request):
    return render(request, 'core/home.html')