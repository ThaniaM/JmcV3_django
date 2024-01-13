from django.shortcuts import render

# Create your views here.
def controlPagos(request):
    return render(request, 'control-pagos.html')