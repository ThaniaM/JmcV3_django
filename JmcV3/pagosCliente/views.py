from django.shortcuts import render

# Create your views here.
def pagosCliente(request):
    return render(request, 'contratos-cliente.html')