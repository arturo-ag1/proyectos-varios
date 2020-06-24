from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime,timedelta,date
from django.db.models.deletion import Collector
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from .models import *

# Create your views here.


def index(request):
    return redirect('/blog/login/')


def login_aux(request):
    print(settings.STATIC_ROOT)
    return redirect('/blog/login/')


def login_page(request):
    return render(request,
                  'login/login.html', {'error': ''})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']

        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            print("si")
            if Usuario.objects.filter(user=user.id).exists():
                rol = Usuario.objects.get(user=user.id)
                request.session['userrol'] = rol.rol.nombre
                print("asldkjasldkjasldjk")
                return redirect('/blog/main/')
            else:
                return render(request,'login/login.html',{'error':'Error de inicio de sesión de usuario, el usuario no existe o las credenciales son incorrectas'})
        else:
            return render(request,'login/login.html', {'error': 'Error de inicio de sesión de usuario, el usuario no existe o las credenciales son incorrectas'})
        
    else:
        return render(request,'login/login.html', {'error': 'You must use POST to login'})
        

def logout_user(request):
    if request.user.is_authenticated():
        return redirect('/blog/login')
    else:
        return redirect('/blog/main')

def main(request):
    return render(request,
                  'main/main.html', {'error': ''})

def usuarios(request):
    return render(request,'usuarios/main.html',{'error':''})

def usuarios_agregar(request):
    return render(request,
                  'usuarios/agregar.html', {'error': ''})

def usuarios_guardar(request):
    if request.method == "POST":

        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        username = request.POST['username']
        password = request.POST['password']

        objUsuario = Usuario.objects.create()

        nuser = User.objects.create_user(username, '', password)
        nuser.last_name = apellido
        nuser.is_active = True
        objUsuario.nombre = nombre
        objUsuario.user= nuser
        objUsuario.apellido = apellido
        objUsuario.telefono = telefono

        objUsuario.save()
        return render(request,'usuarios/main.html',{'error':'','hecho':True})
    else:
        return render(request,'usuarios/main.html',{'error':True})

def usuarios_editar(request,id_tipo):
    if Usuario.objects.filter(id=id_tipo).exists():
        objUsuario = Usuario.objects.get(id=id_tipo)
        print(objUsuario)
        return render(request,'usuarios/editar.html',{'error':'','obj':objUsuario})
    else:
        return render(request,'usuarios/main.html',{'error':True})

def usuarios_editar_guardar(request):
    if request.method == "POST":
        print(request.POST)
        idUsuario = request.POST['idUsuario']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']

        objUsuario = Usuario.objects.get(id=idUsuario)

        objUsuario.nombre = nombre
        objUsuario.apellido = apellido
        objUsuario.telefono = telefono

        objUsuario.save()
        return render(request,'usuarios/main.html',{'error':'','hecho':True})
    else:
        return render(request,'usuarios/main.html',{'error':True})

def usuarios_eliminar(request,id_tipo):
    if Usuario.objects.filter(id=id_tipo).exists():
        error = False
        objUsuario = Usuario.objects.get(id=id_tipo)
        print(objUsuario)

        collector = Collector(using='default')
        try:
            collector.collect([Usuario])
        except Exception as e:
            error = True
            print(e)
        return render(request,'usuarios/eliminar.html',{'error':error,'obj':objUsuario})
    else:
        return render(request,'usuarios/main.html',{'error':True})

def usuarios_eliminar_ok(request):
    if request.method == "POST":
        idUsuario = request.POST['idUsuario']

        objUsuario = Usuario.objects.get(id=idUsuario)
        objUsuario.delete()
        return render(request,'usuarios/main.html',{'error':'','hecho':True})

def clientes(request):
    return render(request,'clientes/main.html',{'error':''})

def clientes_agregar(request):
    estados = Estado.objects.all()
    ciudades = Ciudad.objects.all()
    return render(request,
                  'clientes/agregar.html', {'error': '','estados':estados,'ciudades':ciudades})

def clientes_guardar(request):
    if request.method == "POST":

        codigo = request.POST['codigo']
        razonsocial = request.POST['razonsocial']
        rfc = request.POST['rfc']
        estado = request.POST['estado']
        ciudad = request.POST['ciudad']
        calle = request.POST['calle']
        numeroexterior = request.POST['nexterior']
        numerointerior = request.POST['ninterior']
        cp = request.POST['cp']
        direccioncompleta = request.POST['direccion']

        objCliente = Cliente.objects.create()

        objCliente.codigo = codigo
        objCliente.razonsocial = razonsocial
        objCliente.rfc = rfc
        #objCliente.estado = Estado.objects.get(id=estado)
        #objCliente.ciudad = Ciudad.objects.get(id=ciudad)
        objCliente.calle = calle
        objCliente.numeroexterior = numeroexterior
        objCliente.numerointerior = numerointerior
        objCliente.cp = cp
        objCliente.direccioncompleta = direccioncompleta
        
        objCliente.save()
        return render(request,'clientes/main.html',{'error':'','hecho':True})
    else:
        return render(request,'clientes/main.html',{'error':True})

def clientes_editar(request,id_tipo):
    if Cliente.objects.filter(id=id_tipo).exists():
        objCliente = Cliente.objects.get(id=id_tipo)
        print(objCliente)
        return render(request,'clientes/editar.html',{'error':'','obj':objCliente})
    else:
        return render(request,'clientes/main.html',{'error':True})

def clientes_editar_guardar(request):
    if request.method == "POST":
        print(request.POST)
        idCliente = request.POST['idCliente']
        codigo = request.POST['codigo']
        razonsocial = request.POST['razonsocial']
        rfc = request.POST['rfc']
        estado = request.POST['estado']
        ciudad = request.POST['ciudad']
        calle = request.POST['calle']
        numeroexterior = request.POST['nexterior']
        numerointerior = request.POST['ninterior']
        cp = request.POST['cp']
        direccioncompleta = request.POST['direccion']

        objCliente = Cliente.objects.get(id=idCliente)

        objCliente.codigo = codigo
        objCliente.razonsocial = razonsocial
        objCliente.rfc = rfc
        #objCliente.estado = Estado.objects.get(id=estado)
        #objCliente.ciudad = Ciudad.objects.get(id=ciudad)
        objCliente.calle = calle
        objCliente.numeroexterior = numeroexterior
        objCliente.numerointerior = numerointerior
        objCliente.cp = cp
        objCliente.direccioncompleta = direccioncompleta

        objCliente.save()
        return render(request,'clientes/main.html',{'error':'','hecho':True})
    else:
        return render(request,'clientes/main.html',{'error':True})

def clientes_eliminar(request,id_tipo):
    if Cliente.objects.filter(id=id_tipo).exists():
        error = False
        objCliente = Cliente.objects.get(id=id_tipo)
        print(objCliente)

        collector = Collector(using='default')
        try:
            collector.collect([Usuario])
        except Exception as e:
            error = True
            print(e)
        return render(request,'clientes/eliminar.html',{'error':error,'obj':objCliente})
    else:
        return render(request,'clientes/main.html',{'error':True})

def clientes_eliminar_ok(request):
    if request.method == "POST":
        idCliente = request.POST['idCliente']

        objCliente = Usuario.objects.get(id=idCliente)
        objCliente.delete()
        return render(request,'clientes/main.html',{'error':'','hecho':True})


def sucursales(request):
    return render(request,'sucursales/main.html',{'error':''})

def sucursales_agregar(request):
    clientes = Cliente.objects.all()
    estados = Estado.objects.all()
    ciudades = Ciudad.objects.all()
    return render(request,
                  'sucursales/agregar.html', {'error': '','clientes':clientes,'estados':estados,'ciudades':ciudades})

def sucursales_guardar(request):
    if request.method == "POST":

        codigo = request.POST['codigo']
        cliente = request.POST['cliente']
        representante = request.POST['representante']
        estado = request.POST['estado']
        ciudad = request.POST['ciudad']

        calle = request.POST['calle']
        numeroexterior = request.POST['nexterior']
        numerointerior = request.POST['ninterior']
        cp = request.POST['cp']

        objSucursal = Sucursal.objects.create()

        objSucursal.codigo = codigo
        objSucursal.cliente = Cliente.objects.get(id=cliente)
        objSucursal.representante = representante
        objSucursal.estado = Estado.objects.get(id=estado)
        objSucursal.ciudad = Ciudad.objects.get(id=ciudad)
        objSucursal.calle = calle
        objSucursal.numeroexterior = numeroexterior
        objSucursal.numerointerior = numerointerior
        objSucursal.cp = cp
        
        objSucursal.save()
        return render(request,'sucursales/main.html',{'error':'','hecho':True})
    else:
        return render(request,'sucursales/main.html',{'error':True})

def sucursales_editar(request,id_tipo):
    if Sucursal.objects.filter(id=id_tipo).exists():
        objSucursal = Sucursal.objects.get(id=id_tipo)
        print(objSucursal)

        estados = Estado.objects.all()
        ciudades = Ciudad.objects.all()
        estado = objSucursal.estado
        ciudad = objSucursal.ciudad
        clientes = Cliente.objects.all()
        cliente = objSucursal.cliente
        return render(request,'sucursales/editar.html',{'error':'','obj':objSucursal,'estados':estados,
            'ciudades':ciudades,'estado':estado,'ciudad':ciudad,'clientes':clientes,'cliente':cliente
            })
    else:
        return render(request,'sucursales/main.html',{'error':True})
def sucursales_editar_guardar(request):
    if request.method == "POST":

        idSucursal = request.POST['idSucursal']
        codigo = request.POST['codigo']
        cliente = request.POST['cliente']
        representante = request.POST['representante']
        estado = request.POST['estado']
        ciudad = request.POST['ciudad']

        calle = request.POST['calle']
        numeroexterior = request.POST['nexterior']
        numerointerior = request.POST['ninterior']
        cp = request.POST['cp']

        objSucursal = Sucursal.objects.get(id=idSucursal)

        objSucursal.codigo = codigo
        objSucursal.cliente = Cliente.objects.get(id=cliente)
        objSucursal.representante = representante
        objSucursal.estado = Estado.objects.get(id=estado)
        objSucursal.ciudad = Ciudad.objects.get(id=ciudad)
        objSucursal.calle = calle
        objSucursal.numeroexterior = numeroexterior
        objSucursal.numerointerior = numerointerior
        objSucursal.cp = cp
        
        objSucursal.save()
        return render(request,'sucursales/main.html',{'error':'','hecho':True})
    else:
        return render(request,'sucursales/main.html',{'error':True})
def getNewCiudades(request, *args, **kw):    
    
    message = {"error": False, "message": "", "data": []}
    data = []

    try:
        id_obj = request.GET.get("id_obj", None)
        estadoObj = Estado.objects.get(id = id_obj)
        ciudades = Ciudad.objects.filter(estado = estadoObj)
        for o in ciudades:
            data.append({'id': o.id,'nombre': o.nombre})
    except:
        id_obj = []
    
    print(data)
    message['data'] = data
    return JsonResponse(message)

def sucursales_eliminar(request,id_tipo):
    if Sucursal.objects.filter(id=id_tipo).exists():
        error = False
        objSucursal = Sucursal.objects.get(id=id_tipo)
        print(objSucursal)

        collector = Collector(using='default')
        try:
            collector.collect([Usuario])
        except Exception as e:
            error = True
            print(e)
        return render(request,'sucursales/eliminar.html',{'error':error,'obj':objSucursal})
    else:
        return render(request,'sucursales/main.html',{'error':True})

def sucursales_eliminar_ok(request):
    if request.method == "POST":
        idSucursal = request.POST['idSucursal']

        objSucursal = Usuario.objects.get(id=idSucursal)
        objSucursal.delete()
        return render(request,'clientes/main.html',{'error':'','hecho':True})


def ordenes(request):
    return render(request,'ordenes/main.html',{'error':''})

def ordenes_agregar(request):
    clientes = Cliente.objects.all()
    estados = Estado.objects.all()
    ciudades = Ciudad.objects.all()
    status = StatusOrden.objects.all()
    usuarios = Usuario.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request,
                  'ordenes/agregar.html', {'error': '','clientes':clientes,'estados':estados,'ciudades':ciudades,'status':status,'usuarios':usuarios,'sucursales':sucursales})

def ordenes_guardar(request):
    if request.method == "POST":
        folio = request.POST['folio']
        descripcion = request.POST['descripcion']
        usuario = request.POST['usuario']
        cliente = request.POST['cliente']
        status = request.POST['status']
        sucursal = request.POST['sucursal']
        fecha_limite = request.POST['fecha_limite']

        objOrden = Orden.objects.create()

        objOrden.folio = folio
        objOrden.descripcion = descripcion
        objOrden.usuario = Usuario.objects.get(id=usuario)
        objOrden.cliente = Cliente.objects.get(id=cliente)
        objOrden.status = StatusOrden.objects.get(id=status)
        objOrden.sucursal = Sucursal.objects.get(id=sucursal)
        objOrden.fecha_limite = datetime.strptime(fecha_limite, "%d-%m-%Y")
        objOrden.save()
        return render(request,'ordenes/main.html',{'error':'','hecho':True})
    else:
        return render(request,'ordenes/main.html',{'error':True})

def ordenes_editar(request,id_tipo):
    if Orden.objects.filter(id=id_tipo).exists():
        objOrden = Orden.objects.get(id=id_tipo)
        print(objOrden)

        clientes = Cliente.objects.all()
        cliente = objOrden.cliente
        usuarios = Usuario.objects.all()
        usuario = objOrden.usuario
        status = StatusOrden.objects.all()
        statu = objOrden.status
        sucursales = Sucursal.objects.all()
        sucursal = objOrden.sucursal
        try:
            fecha_limite = objOrden.fecha_limite.strftime("%d-%m-%Y")
        except:
            fecha_limite = ""
        return render(request,'ordenes/editar.html',{'error':'','obj':objOrden,
            'fecha_limite':fecha_limite,
            'clientes':clientes,'cliente':cliente,'usuarios':usuarios,'usuario':usuario,
            'status':status,'statu':statu,'sucursales':sucursales,'sucursal':sucursal
            })
    else:
        return render(request,'ordenes/main.html',{'error':True})

def ordenes_editar_guardar(request):
    if request.method == "POST":
        idOrden = request.POST['idOrden']
        folio = request.POST['folio']
        descripcion = request.POST['descripcion']
        usuario = request.POST['usuario']
        cliente = request.POST['cliente']
        status = request.POST['status']
        sucursal = request.POST['sucursal']
        fecha_limite = request.POST['fecha_limite']

        objOrden = Orden.objects.get(id=idOrden)

        objOrden.folio = folio
        objOrden.descripcion = descripcion
        objOrden.usuario = Usuario.objects.get(id=usuario)
        objOrden.cliente = Cliente.objects.get(id=cliente)
        objOrden.status = StatusOrden.objects.get(id=status)
        objOrden.sucursal = Sucursal.objects.get(id=sucursal)
        objOrden.fecha_limite = datetime.strptime(fecha_limite, "%d-%m-%Y")

        objOrden.save()
        return render(request,'ordenes/main.html',{'error':'','hecho':True})
    else:
        return render(request,'ordenes/main.html',{'error':True})        

def ordenes_eliminar(request,id_tipo):
    if Orden.objects.filter(id=id_tipo).exists():
        error = False
        objOrden = Orden.objects.get(id=id_tipo)
        print(objOrden)

        collector = Collector(using='default')
        try:
            collector.collect([Usuario])
        except Exception as e:
            error = True
            print(e)
        print("orden bien")
        return render(request,'ordenes/eliminar.html',{'error':error,'obj':objOrden})
    else:
        print("error orden")
        return render(request,'ordenes/main.html',{'error':True})

def ordenes_eliminar_ok(request):
    if request.method == "POST":
        idOrden = request.POST['idOrden']

        objOrden = Orden.objects.get(id=idOrden)
        objOrden.delete()
        return render(request,'ordenes/main.html',{'error':'','hecho':True})

def tecnicos(request):
    return render(request,'tecnicos/main.html',{'error':''})

def tecnicos_agregar(request):
    status = StatusTecnico.objects.all()
    tipos = TipoTecnico.objects.all()
    return render(request,
                  'tecnicos/agregar.html', {'error': '','status':status,'tipos':tipos})

def tecnicos_guardar(request):
    if request.method == "POST":

        status = request.POST['status']
        tipo = request.POST['tipo']
        nombre = request.POST['nombre']
        apaterno = request.POST['apaterno']
        amaterno = request.POST['amaterno']
        email = request.POST['email']
        rfc = request.POST['rfc']
        telefono = request.POST['telefono']

        objTecnico = Tecnico.objects.create()

        objTecnico.status = StatusTecnico.objects.get(id=status)
        objTecnico.tipo = TipoTecnico.objects.get(id=tipo)
        objTecnico.nombre = nombre
        objTecnico.apaterno = apaterno
        objTecnico.amaterno = amaterno
        objTecnico.email = email
        objTecnico.rfc = rfc
        objTecnico.telefono = telefono

        objTecnico.save()
        return render(request,'tecnicos/main.html',{'error':'','hecho':True})
    else:
        return render(request,'tecnicos/main.html',{'error':True})

def tecnicos_editar(request,id_tipo):
    if Tecnico.objects.filter(id=id_tipo).exists():
        objTecnico = Tecnico.objects.get(id=id_tipo)
        print(objTecnico)

        status = StatusTecnico.objects.all()
        tipos = TipoTecnico.objects.all()
        statu = objTecnico.status
        tipo = objTecnico.tipo
        return render(request,'tecnicos/editar.html',{'error':'','obj':objTecnico,
            'status':status,'tipos':tipos,'statu':statu,'tipo':tipo
            })
    else:
        return render(request,'tecnicos/main.html',{'error':True})

def tecnicos_editar_guardar(request):
    if request.method == "POST":

        idTecnico = request.POST['idTecnico']
        status = request.POST['status']
        tipo = request.POST['tipo']
        nombre = request.POST['nombre']
        apaterno = request.POST['apaterno']
        amaterno = request.POST['amaterno']
        email = request.POST['email']
        rfc = request.POST['rfc']
        telefono = request.POST['telefono']

        objTecnico = Tecnico.objects.get(id=idTecnico)

        objTecnico.status = StatusTecnico.objects.get(id=status)
        objTecnico.tipo = TipoTecnico.objects.get(id=tipo)
        objTecnico.nombre = nombre
        objTecnico.apaterno = apaterno
        objTecnico.amaterno = amaterno
        objTecnico.email = email
        objTecnico.rfc = rfc
        objTecnico.telefono = telefono

        objTecnico.save()
        return render(request,'tecnicos/main.html',{'error':'','hecho':True})
    else:
        return render(request,'tecnicos/main.html',{'error':True})        

def tecnicos_eliminar(request,id_tipo):
    if Tecnico.objects.filter(id=id_tipo).exists():
        error = False
        objTecnico = Tecnico.objects.get(id=id_tipo)
        print(objTecnico)

        collector = Collector(using='default')
        try:
            collector.collect([Usuario])
        except Exception as e:
            error = True
            print(e)
        print("orden bien")
        return render(request,'tecnicos/eliminar.html',{'error':error,'obj':objTecnico})
    else:
        print("error orden")
        return render(request,'tecnicos/main.html',{'error':True})

def tecnicos_eliminar_ok(request):
    if request.method == "POST":
        idTecnico = request.POST['idTecnico']

        objTecnico = Tecnico.objects.get(id=idTecnico)
        objTecnico.delete()
        return render(request,'tecnicos/main.html',{'error':'','hecho':True})


def pendientes(request):
    usuarios = Usuario.objects.all()
    usuario = Usuario.objects.get(user__id=request.user.id)
    return render(request,'pendientes/main.html',{'error':'','usuarios':usuarios,'usuario':usuario})

def crearTarea(request, *args, **kw):
    message = {"error": False, "message": "", "data": []}
    data = []

    try:
        usuario = request.GET['usuario']
    except:
        usuario = ""
    tarea = request.GET['tarea']

    objTarea = Tarea.objects.create()

    objTarea.descripcion = tarea
    objTarea.pendiente = True
    objTarea.completa = False
    objTarea.cancelada = False

    objTarea.creador = Usuario.objects.get(user__id=request.user.id)

    objTarea.save()

    message['message'] = "Realizado"
    return JsonResponse(message)

def terminarTarea(request, *args, **kw):
    message = {"error": False, "message": "", "data": []}
    data = []

    
    idt = request.GET['id']
    comentario = request.GET['comentario']

    objTarea = Tarea.objects.get(id=idt)

    objTarea.pendiente = False
    objTarea.completa = True
    objTarea.cancelada = False
    
    objTarea.comentario = comentario
    objTarea.fechaterminado = datetime.today()
    objTarea.save()

    message['message'] = "Realizado"
    return JsonResponse(message)

def cancelarTarea(request, *args, **kw):
    message = {"error": False, "message": "", "data": []}
    data = []

    
    idt = request.GET['id']

    objTarea = Tarea.objects.get(id=idt)

    objTarea.pendiente = False
    objTarea.completa = False
    objTarea.cancelada = True
    
    objTarea.fechacancelado = datetime.today()
    objTarea.save()



    message['message'] = "Realizado"
    return JsonResponse(message)

def contactos(request):
    return render(request,
                  'contactos/main.html', {'error': ''})

def contactos_agregar(request):
    estados = Estado.objects.all()
    ciudades = Ciudad.objects.all()
    return render(request,
                  'contactos/agregar.html', {'error': '','estados':estados,'ciudades':ciudades})

def contactos_guardar(request):
    if request.method == "POST":

        estado = request.POST['estado']
        ciudad = request.POST['ciudad']
        nombre = request.POST['nombre']
        puesto = request.POST['puesto']
        email = request.POST['email']
        colonia = request.POST['colonia']
        calle = request.POST['calle']
        telefono = request.POST['telefono']
        cp = request.POST['cp']

        objContacto = Contacto.objects.create()

        objContacto.estado = Estado.objects.get(id=estado)
        objContacto.ciudad = Ciudad.objects.get(id=ciudad)
        objContacto.nombre = nombre
        objContacto.puesto = puesto
        objContacto.email = email
        objContacto.colonia = colonia
        objContacto.calle = calle
        objContacto.telefono = telefono
        objContacto.cp = cp

        objContacto.save()
        return render(request,'contactos/main.html',{'error':'','hecho':True})
    else:
        return render(request,'contactos/main.html',{'error':True})

def contactos_editar(request,id_tipo):
    if Contacto.objects.filter(id=id_tipo).exists():
        objContacto = Contacto.objects.get(id=id_tipo)
        print(objContacto)

        estados = Estado.objects.all()
        ciudades = Ciudad.objects.all()
        estado = objContacto.estado
        ciudad = objContacto.ciudad
        return render(request,'contactos/editar.html',{'error':'','obj':objContacto,
            'estados':estados,'ciudades':ciudades,'estado':estado,'ciudad':ciudad,
            })
    else:
        return render(request,'contactos/main.html',{'error':True})

def contactos_editar_guardar(request):
    if request.method == "POST":

        idContacto = request.POST['idContacto']
        estado = request.POST['estado']
        ciudad = request.POST['ciudad']
        nombre = request.POST['nombre']
        puesto = request.POST['puesto']
        email = request.POST['email']
        colonia = request.POST['colonia']
        calle = request.POST['calle']
        telefono = request.POST['telefono']
        cp = request.POST['cp']

        objContacto = Contacto.objects.get(id=idContacto)

        objContacto.estado = Estado.objects.get(id=estado)
        objContacto.ciudad = Ciudad.objects.get(id=ciudad)
        objContacto.nombre = nombre
        objContacto.puesto = puesto
        objContacto.email = email
        objContacto.colonia = colonia
        objContacto.calle = calle
        objContacto.telefono = telefono
        objContacto.cp = cp

        objContacto.save()
        return render(request,'contactos/main.html',{'error':'','hecho':True})
    else:
        return render(request,'contactos/main.html',{'error':True})        

def contactos_eliminar(request,id_tipo):
    if Contacto.objects.filter(id=id_tipo).exists():
        error = False
        objContacto = Contacto.objects.get(id=id_tipo)
        print(objContacto)

        collector = Collector(using='default')
        try:
            collector.collect([Usuario])
        except Exception as e:
            error = True
            print(e)
        print("orden bien")
        return render(request,'contactos/eliminar.html',{'error':error,'obj':objContacto})
    else:
        print("error orden")
        return render(request,'contactos/main.html',{'error':True})

def contactos_eliminar_ok(request):
    if request.method == "POST":
        idContacto = request.POST['idContacto']

        objContacto = Tecnico.objects.get(id=idContacto)
        objContacto.delete()
        return render(request,'contactos/main.html',{'error':'','hecho':True})



def estadisticas(request):
    totalTareas = Tarea.objects.all().count()

    currentMonth = datetime.now().month
    cantidadClientes = Cliente.objects.all().count()
    cantidadOrdenes = Orden.objects.all().count()
    cantidadTareas = Tarea.objects.filter(creacion__month=currentMonth).count()

    cantidadTerminadas = Tarea.objects.filter(completa=True).count()
    porcentaje = cantidadTerminadas * 100 / totalTareas
    restante = 100 - porcentaje


    return render(request,'estadisticas/main.html',{'error':'','cantidadClientes':cantidadClientes,
        'cantidadOrdenes':cantidadOrdenes,'cantidadTareas':cantidadTareas,'totalTareas':totalTareas,
        'cantidadTerminadas':cantidadTerminadas,'porcentaje':porcentaje,'restante':restante})

def getOrdenes(request, *args, **kw):
    message = {"error": False, "message": "", "data": []}
    data = []
    
    inicio = request.GET['inicio']
    fin = request.GET['fin']
    usuario = Usuario.objects.get(user__id=request.user.id)

    fecha_inicio = datetime.strptime(inicio,"%Y-%m-%d")
    fecha_fin = datetime.strptime(fin,"%Y-%m-%d")


    ordenes = Orden.objects.filter(fecha_limite__gte=fecha_inicio,fecha_limite__lte=fecha_fin)

    print(ordenes)
    for x in ordenes:
        data.append({'id':x.id,
                    'folio':x.folio,
                    'fecha':x.fecha_limite,
                    'url': "",
                    'tipo':"1",
                    })

    message['data'] = data

    message['message'] = "Realizado"
    return JsonResponse(message)