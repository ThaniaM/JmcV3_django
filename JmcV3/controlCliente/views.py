#view 
from django.shortcuts import render
from .forms import ClienteForm
from django.contrib import messages
from .models import Cliente
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # Vincula el formulario con los datos POST
        if form.is_valid():
           
            
            form.save()
            messages.success(request, 'Cliente creado con exito.')
            return redirect('listar')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega mensajes de error detallados
    else:
        form = ClienteForm()  # Crea un objeto vacío 
    return render(request, 'control-clientes.html', {'form': form})

def listar_cliente(request):
    clientes = Cliente.objects.all()
    return render (request, "control-clientes.html", {"clientes":clientes})

def update_cliente(request, id_cliente):
    cliente = get_object_or_404(cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            data = {'message': 'Datos actualizados correctamente'}
            return redirect('listar')
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre':cliente.nombre,
            'correo': cliente.correo,
            'telefono': cliente.telefono,
            'municipio': cliente.municipio,
            'estado': cliente.estado,
            'nom_contacto': cliente.nom_contacto,
            'rfc':cliente.rfc,
            'cp':cliente.cp,
            'direccion':cliente.direccion,
        }
        
        return JsonResponse(data)
@csrf_exempt
def delete_cliente(request, id_cliente):
    if request.method == 'POST':
        try:
            cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
            cliente.delete()
            return JsonResponse({'message': 'Cliente eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
