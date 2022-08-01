from django import views
from django.urls import path
""" from DESPACHOS.api.views import DespachosView, DespachosDetalle, DespachosSearch """

urlpatterns = [
    """ path('despachos-view/', DespachosView.as_view(), name='despachos-view'),
    path('despachos-detalle/<int:id>', DespachosDetalle.as_view(), name='despachos-detalle'),
    path('despachos-search/', DespachosSearch.as_view(), name='despachos-search'), """
]