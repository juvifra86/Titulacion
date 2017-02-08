from django.shortcuts import render,redirect,get_object_or_404,render_to_response
from .forms import PostForm,EventoForm,MensajeForm
from .Magazine import FormNews   
from datetime import datetime
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import usuario,evento,usuario_evento,Inbox,Magazin
import MySQLdb

def index(request):
    return render(request,'EventMate/index.html')#,tareas)

def principal(request):
       nickname=usuario.objects.filter(id=request.user.id)
       return render_to_response('EventMate/principal.html',{'nickname':nickname})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            user=User.objects.create_user(username=request.POST['usuario'],
                                          first_name=request.POST['nombre'],
                                          last_name=request.POST['apellidos'],
                                         email=request.POST['email'],
                                         password=request.POST['contrasena'],)
            user.is_staff=True
            user.save()
            return redirect('EventMate:index')
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        form = PostForm()
    return render(request, 'EventMate/post_edit.html', {'form': form})

def eventos(request):
    try:
        todos_eventos = evento.objects.all()
        mis_eventos=evento.objects.filter(creador_id=request.user.id)
        return render_to_response('EventMate/eventos.html',{'todos_eventos':todos_eventos,'mis_eventos':mis_eventos})
    except:
        return render(request,'EventMate/eventos.html')

def newsletter(request):
    try:
        magas=Magazin.objects.filter(id_usuario=request.user.id)
        return render_to_response('EventMate/newsletter.html',{'magas':magas})
    except:
        return render(request,'EventMate/newsletter.html')

def crearnewsletter(request):
    if request.method == "POST":
        #newss=Magazin.objects.filter(id_usuario=request.user.id)
        form = FormNews(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.id_usuario=request.user.id
            news=form.save()
            return redirect('EventMate:newsletter')
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        #newss=Magazin.objects.filter(id_usuario=request.user.id)
        form = FormNews()
    return render(request, 'EventMate/crearnewsletter.html', {'form': form})
    #try:
        #news=newsletter.objects.filter(id_usuario=request.user.id)
        #return render_to_response('apptitulo/newsletter.html',{'news':news})
    #except:
        #return render(request,'apptitulo/newsletter.html')

def usuarios(request):
    try:
        todos_usuarios=usuario.objects.all()
        return render_to_response('EventMate/usuarios.html',{'todos_usuarios':todos_usuarios})
    except:
        return render(request,'EventMate/principal.html')

def mensajes(request):
    try:
        mensajes_noleidos=Inbox.objects.filter(receptor=request.user.id,stado=0)
        mensajes_leidos=Inbox.objects.filter(receptor=request.user.id,stado=1)
        return render_to_response('EventMate/mensajes.html',{'mensajes_noleidos':mensajes_noleidos,'mensajes_leidos':mensajes_leidos})
    except:
        return render(request,'EventMate/mensajes.html')

def evento_nuevo(request):
    if request.method=="POST":
        forme=EventoForm(request.POST,request.FILES)
        if forme.is_valid():
            #forme.save()
            evento = forme.save(commit=False)
            evento.creador_id=request.user.id
            evento=forme.save()
            return redirect('EventMate:eventos')
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        forme=EventoForm()
    return render(request, 'EventMate/nuevo_evento.html', {'forme': forme})

#def img_evento(request):
   
    #if request.method=="POST":
       # formi=Img_eventoForm(request.POST,request.FILES)
        #if formi.is_valid():
    
            #imgs_evento= formi.save(commit=False)
            #imgs_evento.id_evento=1
            #imgs_evento=formi.save()
            #return redirect('apptitulo:eventos')
        #else:
           # messages.error(request, "Error al procesar el formulario")
    #else:
        #formi=Img_eventoForm()
    #return render(request,'apptitulo/imagenes_eventos.html',{'formi':formi},{'evento':evento})  
    
def detalle_evento(request,pk):
    event = evento.objects.filter(id=pk)
    asistentes = usuario.objects.filter(id__in=usuario_evento.objects.filter(id_evento=pk))
    return render_to_response('EventMate/detalle_evento.html',{'event':event,'asistentes':asistentes})
    
def editar_evento(request,pk):
    post = get_object_or_404(evento, pk=pk)
    if request.method == "POST":
        form = EventoForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.save()
            return redirect('EventMate:detalle_evento', pk=post.pk)
    else:
        form = EventoForm(instance=post)
    return render(request,'EventMate/edit_evento.html', {'form': form})
    #instance = get_object_or_404(evento, id=pk)
    #form = EventoForm(request.POST or None, instance=instance)
    #if form.is_valid():
        #form.save()
        #return redirect('EventMate:eventos')
    #else:
        #return render_to_response('EventMate/edit_evento.html', {'form': form}) 

def unirse_evento(request,pk):
    bd = MySQLdb.connect("localhost","root","kolobos","EventMate")
    cursor=bd.cursor()
    query1='insert into EventMate_usuario_evento(id_evento,id_usuario) values (%s,%s)'%(pk,request.user.id)
    cursor.execute(query1)
    bd.commit()
    bd.close()
    return redirect('EventMate:eventos')

def detalle_usuario(request,pk):
    det_usuario = usuario.objects.filter(id=pk)
    return render_to_response('EventMate/detalle_usuario.html',{'det_usuario':det_usuario})

def esc_mensaje(request):
    if request.method == "POST":
        mens = MensajeForm(request.POST)
        if mens.is_valid():
            mensaje=mens.save(commit=False)
            mensaje.id_remitente=request.user.id
            mensaje=mens.save()
            return redirect('EventMate:mensajes')
        else:
            messages.error(request, "Error al enviar mensaje")
    else:
        mens = MensajeForm()
    return render(request, 'EventMate/esc_mensaje.html', {'mens': mens}) 

def det_mensaje(request,pk):
    mensainbox=Inbox.objects.get(id=pk)
    mensainbox.stado=1
    mensainbox.save()
    mensa = Inbox.objects.filter(id=pk)
    remitente = usuario.objects.filter(id__in=Inbox.objects.filter(id_remitente=pk))
    return render_to_response('EventMate/det_mensaje.html',{'mensa':mensa,'remitente':remitente})