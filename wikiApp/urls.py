from django.urls import path,include
from wikiApp import views


app_name = 'wikiApp'

urlpatterns = [
    path('',views.vistaPrincipal,name = 'vistaPrincipal'),
    path('nuevoarticulo',views.nuevoArt,name = 'nuevoArt'),
    path('nuevotema',views.nuevoTema,name = 'nuevoTema'),
    path('busqueda/',views.busqueda,name= 'busqueda'),
    #se relacionan los urls con los id
    path('articuloTema/<str:idTema>',views.articuloTema,name='articuloTema'),
    path('contenido/<str:idArticulo>',views.contenido,name='contenido'),
    
]
