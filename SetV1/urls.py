"""SetV1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from SetV1 import settings
from AppSetV1 import views
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index, name='index'),
    url(r'^lista/',views.ListaSet_view, name='ListaSet_URLname'),
    url(r'^señales/',views.Señales_view, name='Señales_URLname'),
    url(r'^señalesOsc/',views.SeñalesOsc_view, name='SeñalesOsc_URLname'),
    url(r'^espectro/',views.Espectro_view, name='Espectro_URLname'),
    url(r'^sonido/',views.Sonido_view, name='Sonido_URLname'),
    url(r'^imagen/',views.Imagen_view, name='Imagen_URLname'),
    url(r'^reportes/',views.Reportes_view, name='Reportes_URLname'),
    url(r'^api/data/$',views.get_data, name='get_data_URLname'),

        #Urls para traer elmentos de la base de datos por urls
    url(r'^icono/(?P<icono_id>[0-9]+)', views.IconoGet_view, name='IconoGet_URLname'),
    url(r'^set/(?P<set_id>[0-9]+)', views.SetGet_view, name='SetGet_URLname'),
    url(r'^medicion/(?P<medicion_id>[0-9]+)', views.MedicionGet_view, name='MedicionGet_URLname'),
    url(r'^imagen/(?P<imagen_id>[0-9]+)', views.ImagenGet_view, name='ImagenGet_URLname')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
