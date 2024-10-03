from django import forms
from .models import Cliente, MarcaMotor, MarcaControlador, MarcaModulo, MarcaGenerador, Uso

class ClienteForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all().order_by('nombre_completo'))

class MarcaMotorForm(forms.Form):
    mmotor = forms.ModelChoiceField(queryset=MarcaMotor.objects.all(),label="Marca Motor")

class MarcaControladorForm(forms.Form):
    mcontrolador = forms.ModelChoiceField(queryset=MarcaControlador.objects.all(),label="Marca Controlador")

class MarcaModuloForm(forms.Form):
    mmodulo = forms.ModelChoiceField(queryset=MarcaModulo.objects.all(),label="Marca Modulo")

class MarcaGeneradorForm(forms.Form):
    mgenerador = forms.ModelChoiceField(queryset=MarcaGenerador.objects.all(),label="Marca Generador")

class UsoForm(forms.Form):
    uso = forms.ModelChoiceField(queryset=Uso.objects.all(),label="Uso")
