import json
from django.shortcuts import redirect, render
from .models import Cliente
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


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

def clientes(request):
    clientes = Cliente.objects.filter(cli_id='').order_by('nombre_completo')
    return render(request, 'clientes.html', {"clientes": clientes})

def create_cliente(request):
    grabarubi = request.POST.get('grabarubi')
    if grabarubi:
        cliente = Cliente(nombre_completo=request.POST['nombre_completo'],
                          latitude=request.POST['lat'],
                          longitude=request.POST['lon'])
    else:
        cliente = Cliente(nombre_completo=request.POST['nombre_completo'])
    cliente.save()
    return redirect('clientes')

def delete_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('clientes')

