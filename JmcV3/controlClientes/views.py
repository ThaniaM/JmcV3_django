from django.shortcuts import render
from .forms import ClientesForm
from django.contrib import messages
from .models import Cliente
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_clientes(request):
    # If the request method is POST, process the form data
    return render(request, 'control-clientes.html')

def controlClientes(request):
    return render(request, 'control-clientes.html')


def save_clientes(request):
    form = ClientesForm()  # Mueve la creación del formulario fuera del bloque condicional

    if request.method == 'POST':
            form = ClientesForm(request.POST)  # Crea el formulario con los datos del POST
            if form.is_valid():
                form.save()
                messages.success(request, 'Datos insertados correctamente.')
                return redirect('save')
            else:
                messages.error(request, 'Error al insertar datos. Revise los datos.')
                messages.error(request, form.errors)  # Agrega este mensaje de error para obtener más detalles

    return render(request, 'control-clientes.html', {'form': form})

 
def contact(request):
    if request.method == 'POST':
            form = ClientesForm(request.POST)
            if form.is_valid():
                # Procesa los datos del formulario
                # ...
                messages.success(request, 'Formulario enviado con éxito.')
            else:
                # Muestra un mensaje de error del formulario
                messages.error(request, 'Error en el formulario. Revise los datos.')
                messages.error(request, form.errors)  # Mensajes detallados de error
    else:
        # Muestra el formulario inicial
        form = ClientesForm()
    return render(request, 'control_clientes', {'form': form})
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render (request, "control-clientes.html", {"clientes":clientes})
def update_clientes(request, id_cliente):
    cliente = get_object_or_404(cliente, id_cliente=id_cliente)
    data = {
        'nombre':cliente.nombre,
        'telefono': cliente.telefono,
        'correo': cliente.correo,
        'municipio': cliente.municipio,
        'estado': cliente.estado,
        'nom_contacto': cliente.nom_contacto,
        'rfc':cliente.rfc,
        'rf':cliente.rf,
        'cp':cliente.cp,
        'direccion':cliente.direccion,
    }
    print(data)
    return JsonResponse(data)
@csrf_exempt
def delete_clientes(request, id_cliente):
    if request.method == 'POST':
        try:
            cotizacion = get_object_or_404(Cliente, id_cliente=id_cliente)
            cotizacion.delete()
            return JsonResponse({'message': 'Cliente eliminad correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
