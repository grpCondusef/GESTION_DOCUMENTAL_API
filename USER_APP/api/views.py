from rest_framework.decorators import api_view
from rest_framework.views import APIView  # PARA CREAR VISTAS
from rest_framework import status
from rest_framework.response import Response
from USER_APP.api.serializers import RegistrationSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet  # PARA CREAR VISTAS
#from django.contrib.auth.models import User


# IMPORTAMOS NUESTROS MODELOS AL PANEL DE ADMINISTRACIÓN
from USER_APP.models import User


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'El registro del usuario fue exitoso'
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            data = serializer.errors

        return Response(data)


@api_view(['POST'])
def login_view(request):
    data = {}
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        account = auth.authenticate(username=username, password=password)
        if account is not None:
            data['response'] = 'El Login fue exitoso'
            data['username'] = account.username
            data['uau'] = account.uau
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['error'] = "Credenciales incorrectas"
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data.get('username', ''))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe el usuario'}, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------OBTENER LOS DATOS DEL USUARIO----------------------------------
class GetUserDataView(APIView):

# -------------------------------OBTENER LOS DATOS DEL USUARIO LOGEADO-----------------------
    def get(self, request):
        # DEBE DE LLAMARSE "serializer" Y LE PASAMOS EL USUARIO LOGEADO
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# ----------EDITAR UN REGISTRO EN LA BASE DE DATOS------------------------

    def patch(self, request, id):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            # SI PONEMOS UN "id" QUE NO EXISTE
            return Response({'Error': 'El Usuario no existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # SI ENVÍAMOS DATOS QUE NO SON VÁLIDOS
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
