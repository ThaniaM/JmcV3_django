from django.shortcuts import render

# Create your views here.
def controlContratos(request):
    return render(request, 'control-contratos.html')