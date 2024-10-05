from django.urls import path
from .views import indexep, marcasmotor, create_mmotor, delete_mmotor, marcasgenerador, create_mgenerador, delete_mgenerador, marcasmodulo, create_mmodulo, delete_mmodulo, marcascontrolador, create_mcontrolador, delete_mcontrolador, uso, create_uso, delete_uso, cliugep, actualiza_ubicacion_cliente, equipo, create_equipo, delete_equipo

urlpatterns = [
    path('', indexep, name='indexep'),

    path('marcasmotor/', marcasmotor, name='marcasmotor'),
    path('newmm/', create_mmotor, name='newmm'),
    path('delmm/<int:mmotor_id>/', delete_mmotor, name='delmm'),

    path('marcasgenerador/', marcasgenerador, name='marcasgenerador'),
    path('newmg/', create_mgenerador, name='newmg'),
    path('delmg/<int:mgenerador_id>/', delete_mgenerador, name='delmg'),

    path('marcasmodulo/', marcasmodulo, name='marcasmodulo'),
    path('newmmo/', create_mmodulo, name='newmmo'),
    path('delmmo/<int:mmodulo_id>/', delete_mmodulo, name='delmmo'),

    path('marcascontrolador/', marcascontrolador, name='marcascontrolador'),
    path('newmc/', create_mcontrolador, name='newmc'),
    path('delmc/<int:mcontrolador_id>/', delete_mcontrolador, name='delmc'),

    path('uso/', uso, name='uso'),
    path('newu/', create_uso, name='newu'),
    path('delu/<int:uso_id>/', delete_uso, name='delu'),

    path('cliugep/', cliugep, name='cliugep'),
    path('uptuc/', actualiza_ubicacion_cliente, name='uptuc'),

    path('equiposep/<int:cliente_id>/', equipo, name='equiposep'),
    path('newep/', create_equipo, name='newep'),
    path('delep/<int:equipo_id>/', delete_equipo, name='delep'),
]
