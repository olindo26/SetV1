from django.db import models

#---------------------------------------------ICONOS PARA EL INDEX------------------------------------------------------
class Icono(models.Model):
    nombre=models.CharField(max_length=30)
    iconoimg=models.ImageField(blank=True, null=True)


#-----------------------------------------SUB ESTACIONES TRANSFORMADORAS------------------------------------------------
class SET(models.Model):
    nombre=models.CharField(max_length=20)
    numero=models.IntegerField()
    descripcion=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=50)
    imagen = models.ImageField(blank=True, null=True)
    def __str__(self):
        return '%s %s (%s)' % (self.nombre,self.descripcion,self.ubicacion)
    class Meta:
        verbose_name_plural="Transformadores"


#-------------------------------------VALORES EN BRUTO DE LA ADQUISICIÓN ADS--------------------------------------------
class Adquisicion(models.Model):

    frecuencia = models.FloatField()

    voltage_R = models.FloatField()
    voltage_S = models.FloatField()
    voltage_T = models.FloatField()

    desbalance_U2 = models.FloatField()
    desbalance_U0 = models.FloatField()

    corriente_R = models.FloatField()
    corriente_S = models.FloatField()
    corriente_T = models.FloatField()
    corriente_N = models.FloatField()

    desbalance_I2 = models.FloatField()
    desbalance_I0 = models.FloatField()

    set=models.ForeignKey(SET,on_delete=models.CASCADE,)
    fecha_hora = models.DateTimeField()
    class Meta:
        verbose_name_plural="Adquisiciones"



#------------------------------------------CALCULOS SOBRE LOS BLOQUES DE 200mS------------------------------------------
class Calidad(models.Model):
#___________________________________________________Potencia Aparente___________________________________________________
    Pot_aparente = models.FloatField()
#__________________________________________________Potencia Activa RST__________________________________________________
    Pot_activaVr = models.FloatField()
    Pot_activaVs = models.FloatField()
    Pot_activaVt = models.FloatField()
#_________________________________________________Potencia Reactiva RST_________________________________________________
    Pot_reactivaVr = models.FloatField()
    Pot_reactivaVs = models.FloatField()
    Pot_reactivaVt = models.FloatField()
#_______________________________________________Potencia de Distorcion RST______________________________________________
    Pot_distoVr = models.FloatField()
    Pot_distoVs = models.FloatField()
    Pot_distoVt = models.FloatField()
#________________________________________________Factores de Potencia RST_______________________________________________
    FP_r = models.FloatField()
    FP_s = models.FloatField()
    FP_s = models.FloatField()
#___________________________________________________THD de Tensión RST__________________________________________________
    THD_Vr = models.FloatField()
    THD_Vs = models.FloatField()
    THD_Vt = models.FloatField()
#___________________________________________________THD de Corriente RST________________________________________________
    THD_Ir = models.FloatField()
    THD_Is = models.FloatField()
    THD_It = models.FloatField()
#______________________________________________________Valor Phi RST____________________________________________________
    Phi_r = models.FloatField()
    Phi_s = models.FloatField()
    Phi_t = models.FloatField()
#_____________________________________________________Valor Cos(Phi) RST________________________________________________
    CosPhi_r = models.FloatField()
    CosPhi_s = models.FloatField()
    CosPhi_t = models.FloatField()
#______________________________________________Contenido Armonico de Tension RST________________________________________
    Espectro_Vr = models.TextField()
    Espectro_Vs = models.TextField()
    Espectro_Vt = models.TextField()
#______________________________________________Contenido Armonico de Corriente RSTN_____________________________________
    Espectro_Ir = models.TextField()
    Espectro_Is = models.TextField()
    Espectro_It = models.TextField()
    Espectro_In = models.TextField()
#________________________________________________________Frecuencia_____________________________________________________
    frecuencia = models.FloatField()
#__________________________________________________FechaHora y SETdel paquete___________________________________________
    fecha_hora = models.DateTimeField()
    set=models.ForeignKey(SET,on_delete=models.CASCADE,)
    class Meta:
        verbose_name_plural = "Calidad de Energia"



#--------------------------------------------------Disp and Swells------------------------------------------------------
class dips_swells(models.Model):

    vmin=models.FloatField()
    vmax=models.FloatField()
    duracion=models.FloatField()
    set=models.ForeignKey(SET,on_delete=models.CASCADE,)
    fecha_hora=models.DateTimeField()
    def __str__(self):
        return '%s (%s sg.)' % (self.fecha_hora,self.duracion)
    class Meta:
        verbose_name_plural="Caida y sobrelevacion"


#---------------------------------------------------Interrupciones------------------------------------------------------
class interrupcion(models.Model):
    set=models.ForeignKey(SET,on_delete=models.CASCADE,)
    duracion=models.FloatField()
    fecha_hora=models.DateTimeField()
    def __str__(self):
        return '%s (%s sg.)' % (self.fecha_hora,self.duracion)
    class Meta:
        verbose_name_plural="Interrupciones"




#-----------------------------------------------Cambios rapidos de Tension----------------------------------------------
class rvc(models.Model):
    set = models.ForeignKey(SET,on_delete=models.CASCADE,)
    duracion = models.FloatField()
    fecha_hora = models.DateTimeField()
    def __str__(self):
        return '%s (%s sg.)' % (self.fecha_hora,self.duracion)
    class Meta:
        verbose_name_plural="Cambios rapidos Tension"



#-------------------------------------------------Imagen Termica y Sonido-----------------------------------------------
class img_son(models.Model):
    termico=models.ImageField(upload_to='termica')
    sonido=models.FloatField()
    vibracion=models.FloatField()
    temperatura=models.FloatField()
    set = models.ForeignKey(SET,on_delete=models.CASCADE,)
    fecha_hora = models.DateTimeField()
    def __str__(self):
        return '%s' % (self.fecha_hora)
    class Meta:
        verbose_name_plural="Imagen term y sonido"
