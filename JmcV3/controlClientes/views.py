from django.shortcuts import render, HttpResponse

# Create your views here.
def controlClientes(request):
    return render(request, 'control-clientes.html')