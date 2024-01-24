from django.shortcuts import render #funciones de django
from .forms import ClienteForm #traer el formulario de cliente de la app
from django.contrib import messages#se utiliza para mostrar mensajes
from .models import Cliente #importa el modelo de cliente de la app
from django.shortcuts import render, get_object_or_404, redirect  #indica que va a recuperar un argumento y va a devolver un httpresponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # Vincula el formulario con los datos POST
        if form.is_valid():
            form.save() # Guarda los datos en la base de datos
            messages.success(request, 'Cliente creado con exito.') # Muestra un mensaje de éxito
            return redirect('listar') # Redirige a la página de listado de los clientes
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega mensajes de error detallados
    else:
        form = ClienteForm()  # Crea un objeto vacío 
    return render(request, 'control-clientes.html', {'form': form})# Renderiza la plantilla HTML con el formulario

#funcion para mostrar la lista de los clientes
def listar_cliente(request): #hacemos la solicitud al servidor con la funcion request
    clientes = Cliente.objects.all() #mostramos los clientes almacenaso en la base de datos
    return render (request, "control-clientes.html", {"clientes":clientes}) #respuesta del servidor en la pagina control-clientes

#funcion para actualizar o modificar los datos del cliente
def update_cliente(request, id_cliente): #obtener los datos del cliente mediante el id
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = ClienteForm(request.POST, instance=cliente) #se crea el formulario para la validacion
        if form.is_valid():
            form.save()#si son validos se guardan 
            data = {'message': 'Datos actualizados correctamente'} 
            return redirect('listar') #se regresa al la pagina donde estan los clientes
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre':cliente.nombre,
            #'correo': cliente.correo,
            #'direccion':cliente.direccion,
            #'telefono': cliente.telefono,
            #'rfc':cliente.rfc,
            #'cp':cliente.cp,
            #'municipio': cliente.municipio,
            #'estado': cliente.estado,
            #'nom_contacto': cliente.nom_contacto,
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_cliente(request, id_cliente):
    if request.method == 'POST':
        try:
            cliente = get_object_or_404(Cliente, id_cliente=id_cliente) 
            cliente.delete()
            return JsonResponse({'message': 'Cliente eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)#error en el servidor
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
#get_object_or_404 devueove un objeto o genra una excepcion