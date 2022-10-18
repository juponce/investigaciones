from .forms import SignUpFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy


def login(request):
    return render(request, 'registration/login.html')

class SignUpView(CreateView):
    form_class = SignUpFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'