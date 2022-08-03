from rest_framework import serializers
from REGISTROS_APP.models import RegistrosTable ,ValidacionesTable



class RegistrosSerializer(serializers.ModelSerializer):


    class Meta:
        model = RegistrosTable
        fields = '__all__'


class ValidacionesSerializer(serializers.ModelSerializer):

    #user = UserSerializer(read_only=True) #AGREGAMOS LOS COMENTARIOS A CADA EDIFICACIÓN
    registros = RegistrosSerializer(read_only=True) #AGREGAMOS LOS COMENTARIOS A CADA EDIFICACIÓN

    class Meta:
        model = ValidacionesTable
        fields = '__all__'