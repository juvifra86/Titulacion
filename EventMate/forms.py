from django import forms
from .models import usuario,evento,califica_usuario,Inbox,califica_usuario

class PostForm(forms.ModelForm):

    class Meta:
        model = usuario
        fields = ('nombre',	'apellidos','edad','hobbies','descripcion',
        	'email','usuario','contrasena','pregunta','respuesta','imagen')

class EventoForm(forms.ModelForm):

	class Meta:
		model=evento
		fields=('Titulo','descripcion','Lugar','Fecha','Tipo','Precio','imagen1','imagen2','imagen3')

class MensajeForm(forms.ModelForm):

	class Meta:
		model=Inbox
		fields = ('receptor','mensaje')

class Calif_user(forms.ModelForm):
	class Meta:
		model=califica_usuario
		fields=('calificacion','comentario')


