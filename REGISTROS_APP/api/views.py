from rest_framework.views import APIView
from rest_framework.response import Response #PARA TRAER INFORMACIÓN DE LA BD
from rest_framework import status, generics, filters #PARA MANDAR EL ESTATUS DEL REQUEST, VISTAS GENÉRICAS Y BÚSQUEDAS
from REGISTROS_APP.models import RegistrosTable, ValidacionesTable #EL MODEL DE BD DE LAS TABLAS DE LA BD
from REGISTROS_APP.api.serializers import RegistrosSerializer, ValidacionesSerializer
from USER_APP.models import User


class RegistrosView(APIView):


# ----------OBTENER TODOS LOS REGISTROS DE LA BASE DE DATOS------------------------
    def get(self, request):    
        registros = RegistrosTable.objects.all() #TRAEMOS LOS REGISTROS UNICAMENTE DE EL USUARIO LOGEADO
        serializer = RegistrosSerializer(registros, many=True)
        return Response(serializer.data)

    # ----------AGREGAR UN NUEVO REGISTRO A LA BASE DE DATOS------------------------
    def post(self, request):
        serializer = RegistrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)



class RegistrosDetalle(APIView):

    # ----------ELIMINAR UN REGISTRO DE LA BASE DE DATOS------------------------
    def delete(self, request, id):
        try:
            registros = RegistrosTable.objects.get(pk=id)
        except RegistrosTable.DoesNotExist:
            # SI PONEMOS UN "id" QUE NO EXISTE
            return Response({'Error': 'El registro no existe'}, status=status.HTTP_404_NOT_FOUND)
        registros.delete()
        # CONFIRMAMOS QUE LA OPERACIÓN SE REALIZÓ, PERO NO HAY NADA QUE MOSTRAR
        return Response(status=status.HTTP_204_NO_CONTENT)



# VISTA PARA LA BÚSQUEDA DE REGISTROS, PERO RETORNA SOLAMENTE LOS DEL USUARIO LOGEADO
class RegistrosSearch(generics.ListAPIView):

    serializer_class = RegistrosSerializer

    # -----------------FILTRAMOS LOS REGISTROS DEL USUARIO------------------------------------------
    def get_queryset(self):
        user = self.request.user # OBTENEMOS EL USUARIO ACTUAL
        queryset = RegistrosTable.objects.all()

        return queryset
    
    # --------------------------------FILTROS------------------------------------------------------
    filter_backends = [filters.SearchFilter]
    search_fields = ['numero', 'created_at', 'destinatario', 'folio', ]



#=============================VALIDACIONES DE LOS REGISTROS================================

class ValidacionesView(APIView):


# ----------OBTENER TODOS LOS REGISTROS DE LA BASE DE DATOS------------------------
    def get(self, request):    
        validaciones = ValidacionesTable.objects.all() #TRAEMOS LOS REGISTROS UNICAMENTE DE EL USUARIO LOGEADO
        serializer = ValidacionesSerializer(validaciones, many=True)
        return Response(serializer.data)

    # ----------AGREGAR UN NUEVO REGISTRO A LA BASE DE DATOS------------------------
    def post(self, request):
        serializer = ValidacionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)



class ValidacionesDetalle(APIView):

    # ----------ELIMINAR UN REGISTRO DE LA BASE DE DATOS------------------------
    def delete(self, request, id):
        try:
            validaciones = ValidacionesTable.objects.get(pk=id)
        except ValidacionesTable.DoesNotExist:
            # SI PONEMOS UN "id" QUE NO EXISTE
            return Response({'Error': 'El registro no existe'}, status=status.HTTP_404_NOT_FOUND)
        validaciones.delete()
        # CONFIRMAMOS QUE LA OPERACIÓN SE REALIZÓ, PERO NO HAY NADA QUE MOSTRAR
        return Response(status=status.HTTP_204_NO_CONTENT)



# VISTA PARA LA BÚSQUEDA DE REGISTROS, PERO RETORNA SOLAMENTE LOS DEL USUARIO LOGEADO
class ValidacionesSearch(generics.ListAPIView):

    serializer_class = ValidacionesSerializer

    # -----------------FILTRAMOS LOS REGISTROS DEL USUARIO------------------------------------------
    def get_queryset(self):
        user = self.request.user # OBTENEMOS EL USUARIO ACTUAL
        queryset = ValidacionesTable.objects.all()

        return queryset
    
    # --------------------------------FILTROS------------------------------------------------------
    filter_backends = [filters.SearchFilter]
    search_fields = ['numero', 'created_at', 'destinatario', 'folio', ]