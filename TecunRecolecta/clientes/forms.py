from django import forms
from .models import Cliente

class ClienteForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all().order_by('nombre_completo'))
