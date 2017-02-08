from django import forms
from .models import Magazin

class FormNews(forms.ModelForm):
	class Meta:
		model=Magazin
		fields=('Tipo','descripcion')


