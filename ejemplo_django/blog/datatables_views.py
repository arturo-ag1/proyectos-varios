from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q, F
from .models import *
from datetime import datetime,timedelta,date
import json
from operator import and_ 
from django.db.models.functions import Length

class DTUsuarios(BaseDatatableView):
	order_columns = ['id','user__username', 'nombre', 'apellido', 'celular', 'activo', 'rol', '', '']

	def get_initial_queryset(self):
		q = Usuario.objects.all()
		date = self.request.GET.get(u'date', '')
		dateto = self.request.GET.get(u'dateto', '')
		if date != "" and dateto != "":
			date += " 00:00:00"
			dateto += " 23:59:59"
			dates = [date, dateto]
			q = q.filter(creationdate__range=dates)

		return q

	def filter_queryset(self, qs):
		search_global = self.request.POST.get(u'search[value]', None).split("|")
		if len(search_global) > 1:
			if search_global[0] != "":
				fecha_inicio = str(datetime.strptime(str(search_global[0])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__gte=fecha_inicio)
			if search_global[1] != "":
				fecha_fin = str(datetime.strptime(str(search_global[1])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__lte=fecha_fin)
		
		return qs

	def prepare_results(self, qs):
		json_data = []
		print(qs)
		for item in qs:
			json_data.append({
				'usuario': str(item.user),
				'nombre': str(item.nombre),
				'apellido': str(item.apellido),
				'opciones': str("<a class='btn btn-info btn-circle btn-md m-r-6' data-toggle='tooltip' style='background-color: #23629F; padding-top: 14px; border-color: #23629F' title='Editar' href='/blog/usuarios/editar/" + str(item.id) + "';> <i class='fa fa-pencil'></i></a>""<a class='btn btn-info btn-circle btn-nd m-r-6' data-toggle='tooltip' style='background-color: #bf3026; padding-top: 14px; border-color: #bf3026' title='Borrar' href='/blog/usuarios/eliminar/" + str(item.id) + "';> <i class='fa fa-trash'></i></a>"),
			  
			})
		return json_data

class DTClientes(BaseDatatableView):
	order_columns = ['id','user__username', 'nombre', 'apellido', 'celular', 'activo', 'rol', '', '']

	def get_initial_queryset(self):
		q = Cliente.objects.all()
		date = self.request.GET.get(u'date', '')
		dateto = self.request.GET.get(u'dateto', '')
		if date != "" and dateto != "":
			date += " 00:00:00"
			dateto += " 23:59:59"
			dates = [date, dateto]
			q = q.filter(creationdate__range=dates)

		return q

	def filter_queryset(self, qs):
		search_global = self.request.POST.get(u'search[value]', None).split("|")
		if len(search_global) > 1:
			if search_global[0] != "":
				fecha_inicio = str(datetime.strptime(str(search_global[0])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__gte=fecha_inicio)
			if search_global[1] != "":
				fecha_fin = str(datetime.strptime(str(search_global[1])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__lte=fecha_fin)
		
		return qs

	def prepare_results(self, qs):
		json_data = []
		print(qs)
		for item in qs:
			json_data.append({
				'codigo': str(item.codigo),
				'razonsocial': str(item.razonsocial),
				'estado': str(item.estado),
				'ciudad': str(item.ciudad),
				'telefono': str(item.telefono),
				'opciones': str("<a class='btn btn-info btn-circle btn-md m-r-6' data-toggle='tooltip' style='background-color: #23629F; padding-top: 14px; border-color: #23629F' title='Editar' href='/blog/clientes/editar/" + str(item.id) + "';> <i class='fa fa-pencil'></i></a>""<a class='btn btn-info btn-circle btn-nd m-r-6' data-toggle='tooltip' style='background-color: #bf3026; padding-top: 14px; border-color: #bf3026' title='Borrar' href='/blog/clientes/eliminar/" + str(item.id) + "';> <i class='fa fa-trash'></i></a>"),
			  
			})
		return json_data

class DTSucursales(BaseDatatableView):
	order_columns = ['id','user__username', 'nombre', 'apellido', 'celular', 'activo', 'rol', '', '']

	def get_initial_queryset(self):
		q = Sucursal.objects.all()
		date = self.request.GET.get(u'date', '')
		dateto = self.request.GET.get(u'dateto', '')
		if date != "" and dateto != "":
			date += " 00:00:00"
			dateto += " 23:59:59"
			dates = [date, dateto]
			q = q.filter(creationdate__range=dates)

		return q

	def filter_queryset(self, qs):
		search_global = self.request.POST.get(u'search[value]', None).split("|")
		if len(search_global) > 1:
			if search_global[0] != "":
				fecha_inicio = str(datetime.strptime(str(search_global[0])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__gte=fecha_inicio)
			if search_global[1] != "":
				fecha_fin = str(datetime.strptime(str(search_global[1])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__lte=fecha_fin)
		
		return qs

	def prepare_results(self, qs):
		json_data = []
		print(qs)
		print("ENTRA")
		print("ENTRA")
		print("ENTRA")
		for item in qs:
			json_data.append({
				'codigo': str(item.codigo),
				'cliente': str(item.cliente),
				'estado': str(item.estado),
				'ciudad': str(item.ciudad),
				'telefono': str(item.telefono),
				'opciones': str("<a class='btn btn-info btn-circle btn-md m-r-6' data-toggle='tooltip' style='background-color: #23629F; padding-top: 14px; border-color: #23629F' title='Editar' href='/blog/sucursales/editar/" + str(item.id) + "';> <i class='fa fa-pencil'></i></a>""<a class='btn btn-info btn-circle btn-nd m-r-6' data-toggle='tooltip' style='background-color: #bf3026; padding-top: 14px; border-color: #bf3026' title='Borrar' href='/blog/sucursales/eliminar/" + str(item.id) + "';> <i class='fa fa-trash'></i></a>"),
			  
			})
		return json_data

class DTOrden(BaseDatatableView):
	order_columns = ['id','user__username', 'nombre', 'apellido', 'celular', 'activo', 'rol', '', '']

	def get_initial_queryset(self):
		q = Orden.objects.all()
		date = self.request.GET.get(u'date', '')
		dateto = self.request.GET.get(u'dateto', '')
		if date != "" and dateto != "":
			date += " 00:00:00"
			dateto += " 23:59:59"
			dates = [date, dateto]
			q = q.filter(creationdate__range=dates)

		return q

	def filter_queryset(self, qs):
		search_global = self.request.POST.get(u'search[value]', None).split("|")
		if len(search_global) > 1:
			if search_global[0] != "":
				fecha_inicio = str(datetime.strptime(str(search_global[0])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__gte=fecha_inicio)
			if search_global[1] != "":
				fecha_fin = str(datetime.strptime(str(search_global[1])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__lte=fecha_fin)
		
		return qs

	def prepare_results(self, qs):
		json_data = []
		for item in qs:

			try:
				fecha = item.fecha_limite.strftime("%d-%m-%Y")
			except:
				fecha = ""
			json_data.append({
				'codigo': str(item.folio),
				'status': str(item.status),
				'usuario': str(item.usuario),
				'cliente': str(item.cliente),
				'sucursal': str(item.sucursal),
				'fecha_limite': str(fecha),
				'opciones': str("<a class='btn btn-info btn-circle btn-md m-r-6' data-toggle='tooltip' style='background-color: #23629F; padding-top: 14px; border-color: #23629F' title='Editar' href='/blog/ordenes/editar/" + str(item.id) + "';> <i class='fa fa-pencil'></i></a>""<a class='btn btn-info btn-circle btn-nd m-r-6' data-toggle='tooltip' style='background-color: #bf3026; padding-top: 14px; border-color: #bf3026' title='Borrar' href='/blog/ordenes/eliminar/" + str(item.id) + "';> <i class='fa fa-trash'></i></a>"),
			  
			})
		return json_data

class DTTecnico(BaseDatatableView):
	order_columns = ['id','user__username', 'nombre', 'apellido', 'celular', 'activo', 'rol', '', '']

	def get_initial_queryset(self):
		q = Tecnico.objects.all()
		date = self.request.GET.get(u'date', '')
		dateto = self.request.GET.get(u'dateto', '')
		if date != "" and dateto != "":
			date += " 00:00:00"
			dateto += " 23:59:59"
			dates = [date, dateto]
			q = q.filter(creationdate__range=dates)

		return q

	def filter_queryset(self, qs):
		search_global = self.request.POST.get(u'search[value]', None).split("|")
		if len(search_global) > 1:
			if search_global[0] != "":
				fecha_inicio = str(datetime.strptime(str(search_global[0])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__gte=fecha_inicio)
			if search_global[1] != "":
				fecha_fin = str(datetime.strptime(str(search_global[1])[0:10],"%m/%d/%Y"))
				qs = qs.filter(fecha__lte=fecha_fin)
		
		return qs

	def prepare_results(self, qs):
		json_data = []
		for item in qs:
			json_data.append({
				'nombre': str(item.nombre),
				'apaterno': str(item.apaterno),
				'amaterno': str(item.amaterno),
				'correo': str(item.email),
				'telefono': str(item.telefono),
				'opciones': str("<a class='btn btn-info btn-circle btn-md m-r-6' data-toggle='tooltip' style='background-color: #23629F; padding-top: 14px; border-color: #23629F' title='Editar' href='/blog/tecnicos/editar/" + str(item.id) + "';> <i class='fa fa-pencil'></i></a>""<a class='btn btn-info btn-circle btn-nd m-r-6' data-toggle='tooltip' style='background-color: #bf3026; padding-top: 14px; border-color: #bf3026' title='Borrar' href='/blog/tecnicos/eliminar/" + str(item.id) + "';> <i class='fa fa-trash'></i></a>"),
			})
		return json_data

class DTTareas(BaseDatatableView):
    
    def get_initial_queryset(self):
        id_usuario = self.request.POST['test']
        id_logueado = self.request.POST['id_logueado']

        q = Tarea.objects.all().exclude(cancelada=True)

        return q

    def prepare_results(self, qs):
        id_logueado = self.request.POST['id_logueado']
        json_data = []
        for item in qs:
            if item.pendiente:
                descripcion = "Pendiente"
                if id_logueado == str(item.creador.id):
                    opciones = "<a target='_blank' onclick='completarTarea(" + str(item.id) + ")'; class='btn btn-circle btn-lg m-r-5' data-toggle='tooltip' title='Completar' style='background-color: #23629F; padding-top: 14px; border-color: #23629F'><i class='fa fa-check' style='color: white;'></i></a>"+"<a target='_blank' onclick='cancelarTarea(" + str(item.id) + ")'; class='btn btn-circle btn-lg m-r-5' data-toggle='tooltip' title='Cerrar' style='background-color: #23629F; padding-top: 14px; border-color: #23629F'><i class='fa fa-close' style='color: white;'></i></a>"
                else:
                    opciones = "<a target='_blank' onclick='completarTarea(" + str(item.id) + ")'; class='btn btn-circle btn-lg m-r-5' data-toggle='tooltip' title='Completar' style='background-color: #23629F; padding-top: 14px; border-color: #23629F'><i class='fa fa-check' style='color: white;'></i></a>"+"<a target='_blank' onclick='cancelarTarea(" + str(item.id) + ")'; class='btn btn-circle btn-lg m-r-5' data-toggle='tooltip' title='Cerrar' style='background-color: #23629F; padding-top: 14px; border-color: #23629F'><i class='fa fa-close' style='color: white;'></i></a>"
            elif item.completa:
                descripcion = "Completa"
                opciones = "<a target='_blank' disabled onclick='completarTarea(" + str(item.id) + ")'; class='btn btn-circle btn-lg m-r-5' data-toggle='tooltip' title='Completar' style='background-color: #23629F; padding-top: 14px; border-color: #23629F'><i class='fa fa-check' style='color: white;'></i></a>"+"<a target='_blank' onclick='cancelarTarea(" + str(item.id) + ")'; class='btn btn-circle btn-lg m-r-5' data-toggle='tooltip' title='Cerrar' style='background-color: #23629F; padding-top: 14px; border-color: #23629F'><i class='fa fa-close' style='color: white;'></i></a>"
            else:
                descripcion = "Cancelada"
                opciones = "<a target='_blank' disabled onclick='completarTarea(" + str(item.id) + ")'; class='btn btn-circle btn-lg m-r-5' data-toggle='tooltip' title='Completar' style='background-color: #23629F; padding-top: 14px; border-color: #23629F'><i class='fa fa-check' style='color: white;'></i></a>"+"<a target='_blank' disabled onclick='cancelarTarea(" + str(item.id) + ")'; class='btn btn-circle btn-lg m-r-5' data-toggle='tooltip' title='Cerrar' style='background-color: #23629F; padding-top: 14px; border-color: #23629F'><i class='fa fa-close' style='color: white;'></i></a>"
            
            json_data.append({
                'folio': str(item.id),
                'tarea': str(item.descripcion),
                'creador': str((item.creador.nombre + " "+item.creador.apellido)),
                'estado': descripcion,
                'fecha': "",
                'opciones': opciones,
            })

        return json_data

class DTContacto(BaseDatatableView):
    
    def get_initial_queryset(self):

        q = Contacto.objects.all()

        return q

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            json_data.append({
                'folio': str(item.id),
                'nombre': str(item.nombre),
                'puesto':str(item.puesto),
                'email':str(item.email),
                'telefono':str(item.email),
                'estado':str(item.estado),
                'ciudad':str(item.ciudad),
                'opciones': str("<a class='btn btn-info btn-circle btn-md m-r-6' data-toggle='tooltip' style='background-color: #23629F; padding-top: 14px; border-color: #23629F' title='Editar' href='/blog/contactos/editar/" + str(item.id) + "';> <i class='fa fa-pencil'></i></a>""<a class='btn btn-info btn-circle btn-nd m-r-6' data-toggle='tooltip' style='background-color: #bf3026; padding-top: 14px; border-color: #bf3026' title='Borrar' href='/blog/contactos/eliminar/" + str(item.id) + "';> <i class='fa fa-trash'></i></a>"),
			})

        return json_data