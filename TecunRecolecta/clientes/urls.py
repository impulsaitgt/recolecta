from django.urls import path, include
from .views import marcasmotor, create_mmotor, delete_mmotor, marcasgenerador, create_mgenerador, delete_mgenerador, marcasmodulo, create_mmodulo, delete_mmodulo, marcascontrolador, create_mcontrolador, delete_mcontrolador, opciones, map_view, actualiza_ubicacion_cliente, equipo, uso, create_uso, delete_uso, create_equipo, delete_equipo
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('marcasmotor/', marcasmotor, name='marcasmotor'),
    path('newmm/', create_mmotor, name='newmm'),
    path('delmm/<int:mmotor_id>/', delete_mmotor, name='delmm'),

    path('marcasgenerador/', marcasgenerador, name='marcasgenerador'),
    path('newmg/', create_mgenerador, name='newmg'),
    path('delmg/<int:mgenerador_id>/', delete_mgenerador, name='delmg'),

    path('marcasmodulo/', marcasmodulo, name='marcasmodulo'),
    path('newmmo/', create_mmodulo, name='newmmo'),
    path('delmmo/<int:modulo_id>/', delete_mmodulo, name='delmmo'),

    path('marcascontrolador/', marcascontrolador, name='marcascontrolador'),
    path('newmc/', create_mcontrolador, name='newmc'),
    path('delmc/<int:mcontrolador_id>/', delete_mcontrolador, name='delmc'),

    path('uso/', uso, name='uso'),
    path('newu/', create_uso, name='newu'),
    path('delu/<int:uso_id>/', delete_uso, name='delu'),

    path('opciones/', opciones, name='opciones'),
    path('map/<int:cliente_id>/', map_view, name='map_view'),
    path('uptuc/', actualiza_ubicacion_cliente, name='uptuc'),

    path('equipos/<int:cliente_id>/', equipo, name='equipos'),
    path('newe/', create_equipo, name='newe'),
    path('dele/<int:equipo_id>/', delete_equipo, name='dele'),

]
