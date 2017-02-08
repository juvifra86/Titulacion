from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'EventMate'

urlpatterns = [
   url(r'^$',login,{'template_name':'EventMate/index.html'},name='index'),
   url(r'^usuario/nuevo/$', views.post_new, name='post_new'),
   url(r'^principal/$', views.principal,name='principal'),
   url(r'^$',logout,{'template_name':'EventMate/index.html'},name='logout'),
   url(r'^eventos/$', views.eventos,name='eventos'),
   url(r'^newsletter/$', views.newsletter,name='newsletter'),
   url(r'^usuarios/$', views.usuarios,name='usuarios'),
   url(r'^mensajes/$', views.mensajes,name='mensajes'),
   url(r'^evento/nuevo/$', views.evento_nuevo, name='evento_nuevo'),
   url(r'^detalle_evento/(?P<pk>[0-9]+)/$', views.detalle_evento, name='detalle_evento'),
   url(r'^editar_evento/(?P<pk>[0-9]+)/$', views.editar_evento, name='editar_evento'),
   url(r'^unirse_evento/(?P<pk>[0-9]+)/$', views.unirse_evento, name='unirse_evento'),
   url(r'^detalle_usuario/(?P<pk>[0-9]+)/$', views.detalle_usuario, name='detalle_usuario'),
   url(r'^escribir_mensaje/$', views.esc_mensaje, name='esc_mensaje'),
   url(r'^detalle_mensaje/(?P<pk>[0-9]+)/$', views.det_mensaje, name='det_mensaje'),
   url(r'^nuevo_news/$', views.crearnewsletter, name='crearnewsletter'),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

