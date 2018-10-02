from django.contrib import admin

from AppSetV1.models import Icono,SET, dips_swells, interrupcion, rvc, img_son,Calidad,Adquisicion

class SETAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','ubicacion')
    search_fields=('nombre','descripcion','ubicacion')

class dips_swellsAdmin(admin.ModelAdmin):
    list_filter=('fecha_hora',)

class interrupcionAdmin(admin.ModelAdmin):
    list_filter=('fecha_hora',)

class rvcAdmin(admin.ModelAdmin):
    list_filter=('fecha_hora',)

class img_sonAdmin(admin.ModelAdmin):
    list_filter=('fecha_hora',)

# Register your models here.
admin.site.register(Icono)
admin.site.register(SET,SETAdmin)
admin.site.register(Adquisicion)
admin.site.register(Calidad)
admin.site.register(dips_swells,dips_swellsAdmin)
admin.site.register(interrupcion,interrupcionAdmin)
admin.site.register(rvc,rvcAdmin)
admin.site.register(img_son,img_sonAdmin)
