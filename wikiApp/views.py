from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import temaWiki, articuloWiki
from django.db.models import Q

# Create your views here.

def vistaPrincipal(request):
    listaTemas = temaWiki.objects.all().order_by('id')
    listaTitulos = articuloWiki.objects.all()
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('wikiApp:vistaPrincipal'))
    return render(request,'principal.html',{
        'listaTemas':listaTemas,
        'listaTitulos':listaTitulos,
    })

# names:
# tituloArticulo,Articulo
#devuelve la vista donde se regista un articulo
def nuevoArt(request):
    listaTemas = temaWiki.objects.all().order_by('id')
    if request.method == 'POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        Articulo = request.POST.get('Articulo')
        seleccionTema = request.POST.get('seleccionTema')
        temaRelacionado = temaWiki.objects.get(id=seleccionTema)
        objArticulo = articuloWiki.objects.create(
            tituloArticulo = tituloArticulo,
            Articulo = Articulo,
            temaRelacionado = temaRelacionado,
        )
        objArticulo.save()
        return HttpResponseRedirect(reverse('wikiApp:vistaPrincipal'))
    return render(request,'nuevoArticulo.html',{
        'listaTemas':listaTemas,
    })

# names:
# nombreTema,descripcionTema
#devuelve la vista donde se ingresan los nuevos temas
def nuevoTema(request):
    listaTemas = temaWiki.objects.all().order_by('id')
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        objTema = temaWiki.objects.create(
            nombreTema = nombreTema,
            descripcionTema = descripcionTema,
        )
        objTema.save()
        return HttpResponseRedirect(reverse('wikiApp:vistaPrincipal'))
    return render(request,'nuevoTema.html',{
        'listaTemas':listaTemas,
    })

#devuelve la vista de todos los articulos relacionados a un tema
def articuloTema(request,idTema):
    listaTemas = temaWiki.objects.all().order_by('id')
    objTema = temaWiki.objects.get(id=idTema)
    listaArticulos = objTema.articuloWiki_set.all()
    return render(request,'articuloTema.html',{
        'listaTemas':listaTemas,
        'objTema' : objTema,
        'listaArticulos': listaArticulos,
    })

#devuelve la vista de los articulos creados
def contenido(request,idArticulo):
    listaTemas = temaWiki.objects.all().order_by('id')
    objArticulo = articuloWiki.objects.get(id=idArticulo)
    return render(request,'contenido.html',{
        'listaTemas':listaTemas,
        'objArticulo':objArticulo,
    })

#se define la funcion en la que se duvelve la busqueda realizada
def busqueda(request):
    listaTemas = temaWiki.objects.all().order_by('id')
    if request == 'POST':
        buscar = request.POST.get('search')
        lista = articuloWiki.objects.all().filter(tituloArticulo=buscar)
        return render(request,'buscar.html',{
            'post':lista,
            'listaTemas':listaTemas,
        })
    else:
        return HttpResponseRedirect(reverse('wikiApp:vistaPrincipal'))