from django.contrib import admin
# IMPORTAMOS NUESTROS MODELOS AL PANEL DE ADMINISTRACIÓN
from .models import RegistrosTable, ValidacionesTable


# Register your models here.
class RegistrosAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('user', 'tipo_servicio', 'remitente', 'vicepresidencia')
    ordering = ('-created_at',)
    # VAMOS A PODER BUSCAR CON BASE EN LOS SIGUIENTES CAMPOS
    search_fields = ('user', 'tipo_servicio', 'remitente',)


# REGISTRAMOS EL MODELO Article
admin.site.register(RegistrosTable, RegistrosAdmin)


class ValidacionesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('user', 'folio_ms', 'registro', 'validado')
    ordering = ('-created_at',)
    # VAMOS A PODER BUSCAR CON BASE EN LOS SIGUIENTES CAMPOS
    search_fields = ('user', 'folio_ms', 'registro', 'validado',)


# REGISTRAMOS EL MODELO Article
admin.site.register(ValidacionesTable, ValidacionesAdmin)
