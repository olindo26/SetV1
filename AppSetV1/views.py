from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from django.db.models import Q
from django.views.generic import View
#from rest_framework.utils import json

from AppSetV1.models import SET, Adquisicion,dips_swells, interrupcion, rvc, img_son, Icono,Calidad

#Variables globales
#FiltroId_Glob = None
queryset_list_Glob = None
Longitud_Glob = 1


def index(request):
    template = loader.get_template('index2.html')
    context ={

        'AllObjectIcono_Contex': Icono.objects.all()
      }
    return HttpResponse(template.render(context, request))

def ListaSet_view(request):
    template = loader.get_template('ListSet.html')
    context ={
        'ListSet_Contex': SET.objects.all()
    }
    return HttpResponse(template.render(context, request))

def Señales_view(request):
    queryset_list = Adquisicion.objects.all()
    querynum = request.GET.get("numero")
    queryfecha = request.GET.get("fecha")
    if querynum:
        queryset_list = queryset_list.filter(
            Q(set__numero=querynum) &
            Q(fecha_hora__startswith=queryfecha)
            )
    context ={
        'AllObjectCalidad_Contex' : queryset_list,
    }
    return render (request,"MonitorSeñales.html",context)

def SeñalesOsc_view(request):
    global queryset_list_Glob, Longitud_Glob
    queryset_list_Glob = Adquisicion.objects.all()
    querynum = request.GET.get("numero")
    queryfecha = request.GET.get("fecha")
    Longitud_Glob = request.GET.get("long")
    if querynum:
        queryset_list_Glob = queryset_list_Glob.filter(
            Q(set__numero=querynum) &
            Q(fecha_hora__startswith=queryfecha)
            )

    context ={
        'AllObjectCalidad_Contex' : queryset_list_Glob,
    }
    return render (request,"MonitorSeñalesOsc2.html",context)

def Espectro_view(request):
    queryset_list = Calidad.objects.all()
    querynum = request.GET.get("numero")
    queryfecha = request.GET.get("fecha")
    if querynum:
        queryset_list = queryset_list.filter(
            Q(set__numero=querynum) &
            Q(fecha_hora__startswith=queryfecha)
        )

    context = {
        'AllObjectCalidad_Contex': queryset_list,
    }
    return render(request, "MonitorEspectro.html", context)

def Sonido_view(request):
    queryset_list = img_son.objects.all()
    querynum = request.GET.get("numero")
    queryfecha = request.GET.get("fecha")
    if querynum:
        queryset_list = queryset_list.filter(
            Q(set__numero=querynum) &
            Q(fecha_hora__startswith=queryfecha)
        ).distinct()

    context = {
        'AllObjectCalidad_Contex': queryset_list,
    }
    return render(request, "MonitorSonido.html", context)

def Imagen_view(request):
    queryset_list = img_son.objects.all()
    querynum = request.GET.get("numero")
    queryfecha = request.GET.get("fecha")
    if querynum:
        queryset_list = queryset_list.filter(
            Q(set__numero=querynum) &
            Q(fecha_hora__startswith=queryfecha)
        )

    context = {
        'AllObjectImgSon_Contex': queryset_list,
    }
    return render(request, "MonitorImagen.html", context)


def Reportes_view(request):
    queryset_list = img_son.objects.all()
    querynum = request.GET.get("numero")
    queryfecha = request.GET.get("fecha")
    if querynum:
        queryset_list = queryset_list.filter(
            Q(set__numero=querynum) &
            Q(fecha_hora__startswith=queryfecha)
        )

    context = {
        'AllObjectImgSon_Contex': queryset_list,
    }
    return render(request, "Reportes.html", context)

def IconoGet_view(request,icono_id):
    template = loader.get_template('icono.html')
    context={
        'IconoId_Contex': Icono.objects.get(id=icono_id)
    }
    return HttpResponse(template.render(context, request))

def SetGet_view(request,set_id):
    template = loader.get_template('Set.html')
    context={
        'SetId_Contex': SET.objects.get(id=set_id)
    }
    return HttpResponse(template.render(context, request))

def MedicionGet_view(request,medicion_id):
    template = loader.get_template('base.html')
    context={
        'CalidadId_Contex': Calidad.objects.get(id=medicion_id)
    }
    return HttpResponse(template.render(context, request))

def ImagenGet_view(request,imagen_id):
    template = loader.get_template('base.html')
    context={
        'ImagenId_Contex': img_son.objects.get(id=imagen_id)
    }
    return HttpResponse(template.render(context, request))

def get_data(request,*args,**kwargs):

    global queryset_list_Glob,Longitud_Glob
    Vr=[]
    Vs=[]
    Vt=[]
    Ir=[]
    Is=[]
    It=[]
    In=[]
    for i in range(int(Longitud_Glob)):
        DatFilt = queryset_list_Glob.get(id=i+1)
        Vr.append(DatFilt.voltage_R)
        Vs.append(DatFilt.voltage_S)
        Vt.append(DatFilt.voltage_T)
        Ir.append(DatFilt.corriente_R)
        Is.append(DatFilt.corriente_S)
        It.append(DatFilt.corriente_T)
        In.append(DatFilt.corriente_N)


    data = {

        "labels": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        "VrQuery":Vr,"VsQuery":Vs,"VtQuery":Vt,"IrQuery":Ir,"IsQuery":Is,"ItQuery":It,"InQuery":In,

    }
    return JsonResponse(data)
