from django.shortcuts import render #funciones de django
from .forms import ServicioForm #traer el formulario de servicio de la app
from django.contrib import messages#se utiliza para mostrar mensajes
from .models import Servicio #importa el modelo de servicio de la app
from django.shortcuts import render, get_object_or_404, redirect  #indica que va a recuperar un argumento y va a devolver un httpresponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)  # Vincula el formulario con los datos POST
        if form.is_valid():
            form.save() # Guarda los datos en la base de datos
            messages.success(request, 'Servicio creado con exito.') # Muestra un mensaje de éxito
            return redirect('listar_servicio') # Redirige a la página de listado de los servicio
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega mensajes de error detallados
    else:
        form = ServicioForm()  # Crea un objeto vacío 
    return render(request, 'control-ajuste.html', {'form': form})# Renderiza la plantilla HTML con el formulario

#funcion para mostrar la lista de los servicios
def listar_servicio(request): #hacemos la solicitud al servidor con la funcion request
    servicios = Servicio.objects.all() #mostramos los servicio almacenaso en la base de datos
    return render (request, "control-ajuste.html", {"servicios":servicios}) #respuesta del servidor en la pagina control-ajuste

#funcion para actualizar o modificar los datos del servicio
def update_servicio(request, id_servicio): #obtener los datos del servicio mediante el id
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = ServicioForm(request.POST, instance=servicio) #se crea el formulario para la validacion
        if form.is_valid():
            form.save()#si son validos se guardan 
            data = {'message': 'Datos actualizados correctamente'} 
            return redirect('listar_servicio') #se regresa al la pagina donde estan los servicios
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'nombre_servicio':servicio.nombre_servicio,
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_servicio(request, id_servicio):
    if request.method == 'POST':
        try:
            servicio = get_object_or_404(Servicio, id_servicio=id_servicio) 
            servicio.delete()
            return JsonResponse({'message': 'Servicio eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)#error en el servidor
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
#get_object_or_404 devueove un objeto o genra una excepcion