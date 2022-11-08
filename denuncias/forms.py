from django import forms
from django.forms import ModelForm, DateInput
from .models import *


class DenunciaForm(ModelForm):

    # fecha_delito = forms.DateField(
    #     widget = forms.DateInput(format= '%d%m%Y'),
    #     input_formats = ['%d%m%Y']
    # )

    class Meta:
        model = Denuncia

        fields = ['nombre_denunciante', 'apellido_denunciante', 'rut_denunciante',
            'situacion','descrpción_sospechoso' , 'direccion', 'fecha_delito']

        widgets = {'fecha_delito': forms.DateInput(format='%d/%m/%Y')}

    def __init__(self, *args, **kwargs):
        super(DenunciaForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control radius'