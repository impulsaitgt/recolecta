from django.urls import path, include
from .views import map_view, clientes, create_cliente, delete_cliente
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('map/<int:cliente_id>/', map_view, name='map_view'),

    path('clientes/', clientes, name='clientes'),
    path('newcli/', create_cliente, name='newcli'),
    path('delcli/<int:cliente_id>/', delete_cliente, name='delcli'),


]
