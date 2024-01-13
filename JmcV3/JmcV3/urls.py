"""
URL configuration for JmcV3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login.views import CustomLoginView

#Django settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  #core
    path('', include('core.urls')),
  #ControlStaff
    path('controlStaff/',include('controlStaff.urls')),
  #ControlSoporte
    path('controlSoporte/',include('controlSoporte.urls')),
  #ControlPagos
    path('controlPagos/',include('controlPagos.urls')),
  #ControlContratos
    path('controlContratos/',include('controlContratos.urls')),
  #ControlClientes
    path('controlClientes/',include('controlClientes.urls')),
  #ControlAjuste
    path('controlAjuste/',include('controlAjuste.urls')),
  #Menu Aspel
    path('menuAspel/',include('menuAspel.urls')),
  #Empresa
    path('empresa/' ,include('empresa.urls')),
  #mantenimiento
    path('mantenimiento/' ,include('mantenimiento.urls')),
  #sWeb
    path('sWeb/' ,include('sWeb.urls')),
  #login
    path('login/', CustomLoginView.as_view(), name='login'),
  #admin
    path('admin/', admin.site.urls),

]
