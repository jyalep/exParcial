from django.db import models

# Create your models here.

# names:
# nombreTema,descripcionTema,tituloArticulo,Articulo

class temaWiki(models.Model):
    nombreTema = models.CharField(max_length=128, null=True, blank=True)
    descripcionTema = models.CharField(max_length=512, null=True, blank=True)

class articuloWiki(models.Model):
    tituloArticulo = models.CharField(max_length=128, null=True, blank=True)
    Articulo = models.CharField(max_length=1024, null=True, blank=True)
    temaRelacionado = models.ForeignKey(temaWiki,null = True, blank = True , on_delete = models.SET_NULL)
    
