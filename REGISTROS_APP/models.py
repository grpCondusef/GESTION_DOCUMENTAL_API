from django.db import models
#from django.contrib.auth.models import User #IMPOTAMOS EL MODELO QUE CONTIENE A LOS USUARIOS
from USER_APP.models import User


# Create your models here.
class RegistrosTable(models.Model):

    user = models.ForeignKey(User,editable=False ,verbose_name='Usuario', on_delete=models.CASCADE, null=True) #SI NO PONEMOS LA OPCIÓN DE "null" NOS LO VA A PEDIR AL MOMENTO DE ENVIAR DATOS LA API, SINO NO NOS DEJARÁ HACER NUEVOS REGISTROS
    tipo_servicio = models.CharField(max_length = 110, verbose_name='Tipo de Servicio')
    remitente = models.CharField(max_length = 110, verbose_name='Remitente')
    adscripcion = models.CharField(max_length = 110, verbose_name='Adscripción')
    razon_social = models.CharField(max_length = 110, verbose_name='Razón Social')
    oficio = models.CharField(max_length = 110, verbose_name='Oficio')
    destinatario = models.CharField(max_length = 110, verbose_name='Destinatario')
    num_sepomex = models.CharField(max_length = 110, verbose_name='Número de SEPOMEX', null=True, blank=True)
    estado = models.CharField(max_length = 110, verbose_name='Estado')
    municipio = models.CharField(max_length = 110, verbose_name='Municipio')
    colonia = models.CharField(max_length = 110, verbose_name='Colonia')
    calle = models.CharField(max_length = 110, verbose_name='Calle')
    num_ext = models.CharField(max_length = 110, verbose_name='Número Exterior')
    num_int = models.CharField(max_length = 110, verbose_name='Número Interior', null=True, blank=True)
    tipo_usuario = models.CharField(max_length = 110, verbose_name='Tipo de Usuario')
    asunto = models.CharField(max_length = 110, verbose_name='Asunto')
    vicepresidencia = models.CharField(max_length = 110, verbose_name='Vicepresidencia')
    peso = models.FloatField(max_length = 110, verbose_name='Peso', null=True, blank=True)
    costo = models.FloatField(max_length = 110, verbose_name='Costo', null=True, blank=True)
    folio_diario = models.FloatField(max_length = 110, verbose_name='Folio Diario', null=True, blank=True)
    acuse = models.FileField(upload_to='uploads/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        ordering = ['-created_at'] #ORDENAR PONIENDO PRIMERO LOS ÚLTIMOS ARTÍCULOS PUBLICADOS

    def __str__(self):
        return str(self.user) + ' - ' + self.remitente + ' ' + self.vicepresidencia


class ValidacionesTable(models.Model):

    user = models.ForeignKey(User,editable=False ,verbose_name='Usuario', on_delete=models.CASCADE, null=True) #SI NO PONEMOS LA OPCIÓN DE "null" NOS LO VA A PEDIR AL MOMENTO DE ENVIAR DATOS LA API, SINO NO NOS DEJARÁ HACER NUEVOS REGISTROS
    folio_ms = models.FloatField(max_length = 110, verbose_name='Folio MS')
    registro = models.ForeignKey(RegistrosTable,editable=False ,verbose_name='Registro', on_delete=models.CASCADE, null=True, blank=True)
    validado = models.BooleanField(verbose_name='Validado', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')
    
    class Meta:
        verbose_name = 'Validaciones'
        verbose_name_plural = 'Validaciones'
        ordering = ['-created_at'] #ORDENAR PONIENDO PRIMERO LOS ÚLTIMOS ARTÍCULOS PUBLICADOS

    def __str__(self):
        return str(self.user) + ' - ' + self.folio_ms + ' ' + self.registro