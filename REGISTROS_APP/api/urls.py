from django import views
from django.urls import path
from REGISTROS_APP.api.views import RegistrosView, RegistrosDetalle, RegistrosSearch, ValidacionesView, ValidacionesDetalle ,ValidacionesSearch

urlpatterns = [
    path('registros-view/', RegistrosView.as_view(), name='registros-view'),
    path('registros-detalle/<int:id>', RegistrosDetalle.as_view(), name='registros-detalle'),
    path('registros-search/', RegistrosSearch.as_view(), name='registros-search'),


    path('validaciones-view/', ValidacionesView.as_view(), name='validaciones-view'),
    path('validaciones-detalle/<int:id>', ValidacionesDetalle.as_view(), name='validaciones-detalle'),
    path('validaciones-search/', ValidacionesSearch.as_view(), name='validaciones-search'),
]