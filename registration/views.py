from .forms import SignUpFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from verify_email.email_handler import send_verification_email


def login(request):
    return render(request, 'registration/login.html')

class SignUpView(CreateView):
    form_class = SignUpFormWithEmail
    template_name = 'registration/signup.html'


    @classmethod
    def register_user(request,**kwargs):
        if form.is_valid():
            inactive_user = send_verification_email(request, form_class)

    def get_success_url(self):
        return reverse_lazy('home') + '?success'

