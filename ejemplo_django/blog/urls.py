"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from . import views
from .datatables_views import *

urlpatterns = [

    
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^login/auth$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout'),


    #main
    url(r'^main/$', views.main, name='main'),


    #gets
    url(r'^getNewCiudades/$', views.getNewCiudades, name='getNewCiudades'),

    #usuarios
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^usuarios/agregar/$', views.usuarios_agregar, name='usuarios_agregar'),
    url(r'^usuarios/guardar$', views.usuarios_guardar, name='usuarios_guardar'),
    url(r'^usuarios/serverside$', DTUsuarios.as_view(), name='DTUsuarios'),
    url(r'^usuarios/editar/(?P<id_tipo>[-\w]+)$', views.usuarios_editar, name='usuarios_editar'),
    url(r'^usuarios/editar_usuario/guardar$', views.usuarios_editar_guardar, name='usuarios_editar_guardar'),
    url(r'^usuarios/eliminar/(?P<id_tipo>[-\w]+)$', views.usuarios_eliminar, name='usuarios_eliminar'),
    url(r'^usuarios/eliminar/ok$', views.usuarios_eliminar_ok, name='usuarios_eliminar_ok'),

    #clientes
    url(r'^clientes/$', views.clientes, name='usuarios'),
    url(r'^clientes/agregar/$', views.clientes_agregar, name='clientes_agregar'),
    url(r'^clientes/guardar$', views.clientes_guardar, name='clientes_guardar'),
    url(r'^clientes/serverside$', DTClientes.as_view(), name='DTClientes'),
    url(r'^clientes/editar/(?P<id_tipo>[-\w]+)$', views.clientes_editar, name='clientes_editar'),
    url(r'^clientes/editar_cliente/guardar$', views.clientes_editar_guardar, name='clientes_editar_guardar'),
    url(r'^clientes/eliminar/(?P<id_tipo>[-\w]+)$', views.clientes_eliminar, name='usuarios_eliminar'),
    url(r'^clientes/eliminar/ok$', views.clientes_eliminar_ok, name='clientes_eliminar_ok'),
    

    #sucursales
    url(r'^sucursales/$', views.sucursales, name='sucursales'),
    url(r'^sucursales/serverside$', DTSucursales.as_view(), name='DTSucursales'),
    url(r'^sucursales/agregar/$', views.sucursales_agregar, name='sucursales_agregar'),
    url(r'^sucursales/guardar$', views.sucursales_guardar, name='sucursales_guardar'),
    url(r'^sucursales/editar/(?P<id_tipo>[-\w]+)$', views.sucursales_editar, name='sucursales_editar'),
    url(r'^sucursales/editar_sucursal/guardar$', views.sucursales_editar_guardar, name='sucursales_editar_guardar'),
    url(r'^sucursales/eliminar/(?P<id_tipo>[-\w]+)$', views.sucursales_eliminar, name='sucursales_eliminar'),
    url(r'^sucursales/eliminar/ok$', views.sucursales_eliminar_ok, name='sucursales_eliminar_ok'),

    #ordenes
    url(r'^ordenes/$', views.ordenes, name='ordenes'),
    url(r'^ordenes/agregar/$', views.ordenes_agregar, name='ordenes_agregar'),
    url(r'^ordenes/guardar$', views.ordenes_guardar, name='ordenes_guardar'),
    url(r'^ordenes/serverside$', DTOrden.as_view(), name='DTOrden'),
    url(r'^ordenes/editar/(?P<id_tipo>[-\w]+)$', views.ordenes_editar, name='ordenes_editar'),
    url(r'^ordenes/editar_orden/guardar$', views.ordenes_editar_guardar, name='ordenes_editar_guardar'),
    url(r'^ordenes/eliminar/(?P<id_tipo>[-\w]+)$', views.ordenes_eliminar, name='ordenes_eliminar'),
    url(r'^ordenes/eliminar/ok$', views.ordenes_eliminar_ok, name='ordenes_eliminar_ok'),

    #tecnicos
    url(r'^tecnicos/$', views.tecnicos, name='tecnicos'),
    url(r'^tecnicos/agregar/$', views.tecnicos_agregar, name='tecnicos_agregar'),
    url(r'^tecnicos/guardar$', views.tecnicos_guardar, name='tecnicos_guardar'),
    url(r'^tecnicos/serverside$', DTTecnico.as_view(), name='DTTecnico'),
    url(r'^tecnicos/editar/(?P<id_tipo>[-\w]+)$', views.tecnicos_editar, name='ordenes_editar'),
    url(r'^tecnicos/editar_tecnico/guardar$', views.tecnicos_editar_guardar, name='tecnicos_editar_guardar'),
    url(r'^tecnicos/eliminar/(?P<id_tipo>[-\w]+)$', views.tecnicos_eliminar, name='tecnicos_eliminar'),
    url(r'^tecnicos/eliminar/ok$', views.tecnicos_eliminar_ok, name='tecnicos_eliminar_ok'),

    #TAREAS
    url(r'^pendientes/$', views.pendientes, name='pendientes'),
    url(r'^tareas/serverside$', DTTareas.as_view(), name='DTTareas'),
    url(r'^crearTarea$', views.crearTarea, name='crearTarea'),
    url(r'^terminarTarea$', views.terminarTarea, name='terminarTarea'),
    url(r'^cancelarTarea$', views.cancelarTarea, name='cancelarTarea'),

    #contactos
    url(r'^contactos/$', views.contactos, name='contactos'),
    url(r'^contactos/serverside$', DTContacto.as_view(), name='DTContacto'),
    url(r'^contactos/agregar/$', views.contactos_agregar, name='contactos_agregar'),
    url(r'^contactos/guardar$', views.contactos_guardar, name='contactos_guardar'),
    url(r'^contactos/editar/(?P<id_tipo>[-\w]+)$', views.contactos_editar, name='contactos_editar'),
    url(r'^contactos/editar_contacto/guardar$', views.contactos_editar_guardar, name='contactos_editar_guardar'),
    url(r'^contactos/eliminar/(?P<id_tipo>[-\w]+)$', views.contactos_eliminar, name='contactos_eliminar'),
    url(r'^contactos/eliminar/ok$', views.contactos_eliminar_ok, name='contactos_eliminar_ok'),


    #TAREAS
    url(r'^estadisticas/$', views.estadisticas, name='estadisticas'),
    url(r'^getOrdenes/$', views.getOrdenes, name='getOrdenes'),

]
