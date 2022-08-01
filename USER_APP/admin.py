from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User #IMPORTAMOS NUESTROS MODELOS AL PANEL DE ADMINISTRACIÓN

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name', 'is_login', 'is_active' , 'uau', 'is_working') #CAMPOS QUE APARECEN EN LA TABLA DE REGISTROS

admin.site.register(User, UserAdmin)

