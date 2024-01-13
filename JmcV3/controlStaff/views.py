from django.shortcuts import render

# Create your views here.
def controlStaff(request):
    return render(request, 'control-staff.html')