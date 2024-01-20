from django.shortcuts import render

# Create your views here.
def contratosCliente(request):
    return render(request, 'contratos-cliente.html')