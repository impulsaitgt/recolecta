import json
from django.shortcuts import redirect, render
from .models import MarcaMotor, MarcaGenerador, MarcaModulo, MarcaControlador, Cliente, Equipo, Uso
from .forms import ClienteForm, MarcaMotorForm, MarcaControladorForm, MarcaGeneradorForm, MarcaModuloForm, UsoForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def marcasmotor(request):
    mmotors = MarcaMotor.objects.all().order_by('descripcion')
    return render(request, 'marcasmotor.html', {"mmotors": mmotors})

def create_mmotor(request):
    mmotor = MarcaMotor(descripcion=request.POST['descripcion'])
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
    mgenerador = MarcaGenerador(descripcion=request.POST['descripcion'])
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
    mmodulo = MarcaModulo(descripcion=request.POST['descripcion'])
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
    mcontrolador = MarcaControlador(descripcion=request.POST['descripcion'])
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
    uso = Uso(descripcion=request.POST['descripcion'])
    uso.save()
    return redirect('uso')

def delete_uso(request, uso_id):
    uso = Uso.objects.get(id=uso_id)
    uso.delete()
    return redirect('uso')


def opciones(request):
    clientes = ClienteForm()
    return render(request, 'opciones.html', {"clientes": clientes})

@csrf_exempt  # Desactiva la verificación CSRF para simplificar el ejemplo (usa con cuidado)
def save_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        reporter_id = data.get('cliente_id')  # ID del reportero
        latitude = data.get('lat')
        longitude = data.get('lon')

        try:
            print('si pasa?')
            reporter = Cliente.objects.get(id=reporter_id)
            reporter.latitude = latitude
            reporter.longitude = longitude
            reporter.save()
            return JsonResponse({'status': 'Location saved successfully!'})
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Reporter not found'}, status=404)

def map_view(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'map.html', {'cliente': cliente})


def actualiza_ubicacion_cliente(request):
    cliente_id = request.POST['cliente']
    action_type = request.POST['action_type']

    print('action_type: ',action_type)
    if action_type == 'registra_ubicacion':
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.latitude = request.POST['lat']
        cliente.longitude = request.POST['lon']
        cliente.save()
    return redirect('equipos', cliente_id = cliente_id)


def equipo(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    equipos = Equipo.objects.filter(cliente=cliente_id).order_by('descripcion')
    mmotors = MarcaMotorForm()
    mcontroladors = MarcaControladorForm()
    mgeneradors = MarcaGeneradorForm()
    mmodulos = MarcaModuloForm()
    usos = UsoForm()
    return render(request, 'equipos.html', { "cliente": cliente,
                                                                  "equipos": equipos,
                                                                  "mmotors": mmotors,
                                                                  "mcontroladors": mcontroladors,
                                                                  "mgeneradors": mgeneradors,
                                                                  "mmodulos": mmodulos,
                                                                  "usos": usos})


    # Horometro = models.FloatField(null=True, blank=True)
    # latitude = models.FloatField(null=True, blank=True)  # Campo para latitud
    # longitude = models.FloatField(null=True, blank=True)  # Campo para longitud
    # Potencia = models.FloatField(null=True, blank=True)
    # cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # uso = models.ForeignKey(Uso, on_delete=models.CASCADE)
    # marcamotor = models.ForeignKey(MarcaMotor, on_delete=models.CASCADE)
    # marcagenerador = models.ForeignKey(MarcaGenerador, on_delete=models.CASCADE)
    # marcamodulo = models.ForeignKey(MarcaModulo, on_delete=models.CASCADE)
    # marcacontrolador = models.ForeignKey(MarcaControlador, on_delete=models.CASCADE)

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
                        marcacontrolador_id=request.POST['mcontrolador'])
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
                        marcacontrolador_id=request.POST['mcontrolador'])

    equipo.save()
    return redirect('equipos', cliente_id)

def delete_equipo(request, equipo_id):
    cliente_id = request.POST['cliente_id']
    equipo = Equipo.objects.get(id=equipo_id)
    equipo.delete()
    return redirect('equipos', cliente_id)
