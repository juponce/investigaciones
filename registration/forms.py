from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpFormWithEmail(UserCreationForm):
    email = forms.EmailField(max_length=254)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        domain = email.split('@')[1]
        domain_list = ["duocuc.cl", "profesor.duoc.cl"]

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        if domain not in domain_list:
            raise forms.ValidationError("El correo debe ser dominio Duoc")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya se encuentra registrado, prueba con otro")
        if len(username) <= 3:
            raise forms.ValidationError("Nombre de usuario demasiado corto utilizar minimo 4 caracteres")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) <= 7:
            raise forms.ValidationError("Contraseña demasiado corta, debe tener al menos 8 caracteres")
        
        return password1

    def clean_password2(self):

        cleaned_data = super(SignUpFormWithEmail, self).clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        print(password)
        print(confirm_password)

        if password != confirm_password:
            raise forms.ValidationError("Nombre de usuario demasiado corto utilizar minimo 4 caracteres")
        return confirm_password



    def __init__(self, *args, **kwargs):
        super(SignUpFormWithEmail, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control radius'