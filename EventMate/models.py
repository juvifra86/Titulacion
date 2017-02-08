from __future__ import unicode_literals

from django.db import models

from django.core.files.storage import FileSystemStorage

class pregunta(models.Model):
	descripcion = models.CharField(max_length=60)

	def __str__(self):
		return self.descripcion
		
class usuario(models.Model):
	nombre = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60,default='')
	edad = models.IntegerField(default=0)
	hobbies = models.CharField(max_length=60,default='')
	descripcion = models.CharField(max_length=160,default='')
	email = models.EmailField(default='')
	usuario = models.CharField(max_length=60,default='')
	contrasena = models.CharField(max_length=60,default='')
	pregunta = models.ForeignKey(pregunta)
	respuesta = models.CharField(max_length=60,default='')
	imagen=models.FileField(upload_to="mediaf/",blank=True,null=True)

	def __str__(self):
		return self.usuario

class tipo_evento(models.Model):
	descripcion=models.CharField(max_length=60)

	def __str__(self):
		return self.descripcion

class evento(models.Model):
	Titulo=models.CharField(max_length=60)
	creador_id=models.IntegerField(default=0)
	descripcion=models.CharField(max_length=120,default='')
	Lugar=models.CharField(max_length=120)
	Fecha=models.DateTimeField(default='1900-01-01')
	Tipo=models.ForeignKey(tipo_evento)
	Precio=models.FloatField(default=0.0)
	stado=models.IntegerField(default=0)
	init=models.DateTimeField(auto_now_add=True)
	finish=models.DateTimeField(default='1900-01-01')
	imagen1=models.FileField(upload_to="evento_img/",blank=True,null=True)
	imagen2=models.FileField(upload_to="evento_img/",blank=True,null=True)
	imagen3=models.FileField(upload_to="evento_img/",blank=True,null=True)

	def __str__(self):
		return self.descripcion

#class Img_evento(models.Model):
	#id_evento=models.IntegerField(default=0)
	#descripcion=models.CharField(max_length=120,default='')
	#imagen_evento=models.FileField(upload_to="img_evento/",blank=True,null=True)

	#def __str__(self):
		#return self.descripcion
		
class usuario_evento(models.Model):
	id_evento=models.IntegerField(default=0)
	id_usuario=models.IntegerField(default=0)

	def __int__(self):
		return self.id_evento

class Magazin(models.Model):
	id_usuario=models.IntegerField(default=0)
	Tipo=models.ForeignKey(tipo_evento)
	descripcion=models.CharField(max_length=120,default='')

	def __str__(self):
		return self.descripcion 

class Inbox(models.Model):
	id_remitente=models.IntegerField(default=0)
	receptor=models.ForeignKey(usuario)
	mensaje=models.CharField(max_length=120,default='')
	stado=models.IntegerField(default=0)
	init=models.DateTimeField(auto_now_add=True)
	finish=models.DateTimeField(default='1900-01-01')

	def __int__(self):
		return self.id_remitente

class califica_usuario(models.Model):
	id_usuario=models.IntegerField(default=0)
	calificacion=models.IntegerField(default=0)
	comentario=models.CharField(max_length=120,default='')
	#stado=models.IntegerField(default=0)
	init=models.DateTimeField(auto_now_add=True)
	#finish=models.DateTimeField(default='1900-01-01')

	def __int__(self):
		return self.id_usuario
