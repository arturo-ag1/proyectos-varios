from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Cliente)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Sucursal)
admin.site.register(StatusOrden)
admin.site.register(Orden)
admin.site.register(StatusTecnico)
admin.site.register(TipoTecnico)
admin.site.register(Tecnico)
admin.site.register(Tarea)