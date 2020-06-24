from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

#Pruebas iniciales de modelos. Antonio Miravete 15/01/2020.
class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, blank=True, null=True)
    userid = models.CharField(max_length=400,blank=True, null= True)
    nombre = models.CharField(max_length=400, default="")
    apellido = models.CharField(max_length=400, default="")
    celular = models.CharField(max_length=400, default="")
    activo = models.BooleanField(default=True)
    creationdate = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.user.username + "--" + str(self.nombre)

class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=True, null=True)
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre


class TipoCliente(models.Model):
    
    nombre = models.CharField(max_length=400,blank=True, null= True)
    creacion = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return str(self.nombre)

class Cliente(models.Model):
    
    codigo = models.CharField(max_length=400,blank=True, null= True)
    razonsocial = models.CharField(max_length=400,blank=True, null= True)
    rfc = models.CharField(max_length=400,blank=True, null= True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = ChainedForeignKey(
        Ciudad,
        chained_field="estado",
        chained_model_field="estado",
        show_all=False,
        auto_choose=True,
        on_delete=models.PROTECT,blank=True, null=True
    )
    direccioncompleta = models.CharField(max_length=400,blank=True, null= True)
    calle = models.CharField(max_length=400,blank=True, null= True)
    numeroexterior = models.CharField(max_length=400,blank=True, null= True)
    numerointerior = models.CharField(max_length=400,blank=True, null= True)
    cp = models.CharField(max_length=400,blank=True, null= True)
    telefono = models.CharField(max_length=400,blank=True, null= True)
    creacion = models.DateTimeField(default=timezone.now, editable=False)
    lunes = models.BooleanField(default=False)
    martes = models.BooleanField(default=False)
    miercoles = models.BooleanField(default=False)
    jueves = models.BooleanField(default=False)
    viernes = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False) 
    tipocliente = models.ForeignKey(TipoCliente, on_delete=models.PROTECT, blank=True, null=True) 
    email = models.CharField(max_length=400,blank=True, null= True)
    telefono = models.CharField(max_length=400,blank=True, null= True)
    nombrecomercialtxt = models.CharField(max_length=400,blank=True, null= True)

    def __str__(self):
        return str(self.razonsocial)

class Sucursal(models.Model):
    codigo = models.CharField(max_length=400,blank=True,null=True)
    lat = models.CharField(max_length=100,blank=True,null=True)
    lon = models.CharField(max_length=100,blank=True,null=True)
    calle = models.CharField(max_length=400,blank=True, null= True)
    numeroexterior = models.CharField(max_length=400,blank=True, null= True)
    numerointerior = models.CharField(max_length=400,blank=True, null= True)
    cp = models.CharField(max_length=400,blank=True, null= True)
    telefono = models.CharField(max_length=400,blank=True, null= True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, blank=True, null=True) 
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = ChainedForeignKey(
        Ciudad,
        chained_field="estado",
        chained_model_field="estado",
        show_all=False,
        auto_choose=True,
        on_delete=models.PROTECT,blank=True, null=True
    )
    representante = models.CharField(max_length=400,blank=True, null= True)

    def __str__(self):
        return str(self.codigo)

class StatusOrden(models.Model):
    descripcion = models.CharField(max_length=400,blank=True, null= True)
    creacion = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return str(self.descripcion)

class StatusTecnico(models.Model):
    descripcion = models.CharField(max_length=400,blank=True, null= True)
    creacion = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return str(self.descripcion)

class TipoTecnico(models.Model):
    descripcion = models.CharField(max_length=400,blank=True, null= True)
    creacion = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return str(self.descripcion)

class Orden(models.Model):
    folio = models.CharField(max_length=40,blank=True,null=True)
    status = models.ForeignKey(StatusOrden, on_delete=models.PROTECT, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank=True, null=True,related_name='usuario')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, blank=True, null=True)
    descripcion  = models.CharField(max_length=600,blank=True, null= True)
    ocultar = models.BooleanField(default=False)
    fecha_limite = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return str(self.folio)

class Tecnico(models.Model):
    status = models.ForeignKey(StatusTecnico, on_delete=models.PROTECT, blank=True, null=True)
    tipo = models.ForeignKey(TipoTecnico, on_delete=models.PROTECT, blank=True, null=True)
    nombre = models.CharField(max_length=200,blank=True,null=True)
    apaterno = models.CharField(max_length=200,blank=True,null=True)
    amaterno = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=400,blank=True, null= True)
    telefono = models.CharField(max_length=400,blank=True, null= True)
    rfc = models.CharField(max_length=400,blank=True, null= True)
    
    def __str__(self):
        return str(self.nombre)

class Tarea(models.Model): 
    descripcion = models.CharField(max_length=400,blank=True, null= True)
    pendiente = models.BooleanField(default=False)
    completa = models.BooleanField(default=False)
    cancelada = models.BooleanField(default=False)
    creador = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank=True, null=True,related_name='creado')  
    asignado = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank=True, null=True,related_name='asignado')  
    fechalimite = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=400,blank=True, null= True)
    fechacancelado = models.DateTimeField(blank=True, null=True)
    fechaterminado = models.DateTimeField(blank=True, null=True)

    creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)

class Contacto(models.Model):
    
    nombre = models.CharField(max_length=400,blank=True, null= True)
    puesto = models.CharField(max_length=400,blank=True, null= True)
    email = models.CharField(max_length=400,blank=True, null= True)
    telefono = models.CharField(max_length=400,blank=True, null= True)
    extension = models.CharField(max_length=400,blank=True, null= True)
    creacion = models.DateTimeField(default=timezone.now, editable=False)
    #Nuevos por localizacion
    colonia = models.CharField(max_length=400,blank=True, null= True)
    cp = models.CharField(max_length=400,blank=True, null= True)
    calle = models.CharField(max_length=400,blank=True, null= True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = ChainedForeignKey(
        Ciudad,
        chained_field="estado",
        chained_model_field="estado",
        show_all=False,
        auto_choose=True,
        on_delete=models.PROTECT,blank=True, null=True
    )
    def __str__(self):
        return str(self.nombre)
