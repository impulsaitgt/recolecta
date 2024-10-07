from django.shortcuts import render, redirect
from .models import MarcaMotor, MarcaGenerador, MarcaModulo, MarcaControlador, Uso, Equipo
from .forms import MarcaMotorForm, MarcaGeneradorForm, MarcaModuloForm, MarcaControladorForm, UsoForm
from clientes.models import Cliente
from clientes.forms import ClienteForm

# Create your views here.

def indexep(request):
    return render(request, 'indexep.html')

def marcasmotor(request):
    mmotors = MarcaMotor.objects.all().order_by('descripcion')
    return render(request, 'marcasmotor.html', {"mmotors": mmotors})

def create_mmotor(request):
    mmotor = MarcaMotor(descripcion=request.POST['descripcion'],usuario=request.user.username)
    mmotor.save()
    return redirect('marcasmotor')

def delete_mmotor(request, mmotor_id):
    mmotor = MarcaMotor.objects.get(id=mmotor_id)
    mmotor.delete()
    return redirect('marcasmotor')

def marcasgenerador(request):
    mgeneradors = MarcaGenerador.objects.all().order_by('descripcion')
    return render(request, 'marcasgenerador.html', {"mgeneradors": mgeneradors})

def create_mgenerador(request):
    mgenerador = MarcaGenerador(descripcion=request.POST['descripcion'],usuario=request.user.username)
    mgenerador.save()
    return redirect('marcasgenerador')

def delete_mgenerador(request, mgenerador_id):
    mgenerador = MarcaGenerador.objects.get(id=mgenerador_id)
    mgenerador.delete()
    return redirect('marcasgenerador')

def marcasmodulo(request):
    mmodulos = MarcaModulo.objects.all().order_by('descripcion')
    return render(request, 'marcasmodulo.html', {"mmodulos": mmodulos})

def create_mmodulo(request):
    mmodulo = MarcaModulo(descripcion=request.POST['descripcion'],usuario=request.user.username)
    mmodulo.save()
    return redirect('marcasmodulo')

def delete_mmodulo(request, mmodulo_id):
    mmodulo = MarcaModulo.objects.get(id=mmodulo_id)
    mmodulo.delete()
    return redirect('marcasmodulo')


def marcascontrolador(request):
    mcontroladors = MarcaControlador.objects.all().order_by('descripcion')
    return render(request, 'marcascontrolador.html', {"mcontroladors": mcontroladors})

def create_mcontrolador(request):
    mcontrolador = MarcaControlador(descripcion=request.POST['descripcion'],usuario=request.user.username)
    mcontrolador.save()
    return redirect('marcascontrolador')

def delete_mcontrolador(request, mcontrolador_id):
    mcontrolador = MarcaControlador.objects.get(id=mcontrolador_id)
    mcontrolador.delete()
    return redirect('marcascontrolador')

def uso(request):
    usos = Uso.objects.all().order_by('descripcion')
    return render(request, 'uso.html', {"usos": usos})

def create_uso(request):
    uso = Uso(descripcion=request.POST['descripcion'],usuario=request.user.username)
    uso.save()
    return redirect('uso')

def delete_uso(request, uso_id):
    uso = Uso.objects.get(id=uso_id)
    uso.delete()
    return redirect('uso')

def cliugep(request):
    clientes = ClienteForm()
    return render(request, 'cliugep.html', {"clientes": clientes})

def actualiza_ubicacion_cliente(request):
    cliente_id = request.POST['cliente']
    action_type = request.POST['action_type']

    if action_type == 'registra_ubicacion':
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.latitude = request.POST['lat']
        cliente.longitude = request.POST['lon']
        cliente.usuario = request.user.username
        cliente.save()
    return redirect('equiposep', cliente_id = cliente_id)

def equipo(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    equipos = Equipo.objects.filter(cliente=cliente_id).order_by('descripcion')
    mmotors = MarcaMotorForm()
    mcontroladors = MarcaControladorForm()
    mgeneradors = MarcaGeneradorForm()
    mmodulos = MarcaModuloForm()
    usos = UsoForm()
    return render(request, 'equiposep.html', { "cliente": cliente,
                                                                  "equipos": equipos,
                                                                  "mmotors": mmotors,
                                                                  "mcontroladors": mcontroladors,
                                                                  "mgeneradors": mgeneradors,
                                                                  "mmodulos": mmodulos,
                                                                  "usos": usos})

def create_equipo(request):
    cliente_id = request.POST['cliente_id']
    grabarubi = request.POST.get('grabarubi')
    if grabarubi:
        equipo = Equipo(cliente_id=request.POST['cliente_id'],
                        descripcion=request.POST['descripcion'],
                        observaciones=request.POST['observaciones'],
                        Horometro=request.POST['Horometro'],
                        latitude=request.POST['lat'],
                        longitude=request.POST['lon'],
                        Potencia=request.POST['potencia'],
                        uso_id=request.POST['uso'],
                        marcamotor_id=request.POST['mmotor'],
                        marcagenerador_id=request.POST['mgenerador'],
                        marcamodulo_id=request.POST['mmodulo'],
                        marcacontrolador_id=request.POST['mcontrolador'],
                        usuario=request.user.username)
    else:
        equipo = Equipo(cliente_id=request.POST['cliente_id'],
                        descripcion=request.POST['descripcion'],
                        observaciones=request.POST['observaciones'],
                        Horometro=request.POST['Horometro'],
                        Potencia=request.POST['potencia'],
                        uso_id=request.POST['uso'],
                        marcamotor_id=request.POST['mmotor'],
                        marcagenerador_id=request.POST['mgenerador'],
                        marcamodulo_id=request.POST['mmodulo'],
                        marcacontrolador_id=request.POST['mcontrolador'],
                        usuario=request.user.username)

    equipo.save()
    return redirect('equiposep', cliente_id)

def delete_equipo(request, equipo_id):
    cliente_id = request.POST['cliente_id']
    equipo = Equipo.objects.get(id=equipo_id)
    equipo.delete()
    return redirect('equiposep', cliente_id)