from django.urls import path

from .views import *
from sigss_principal.plataforma.views import *
# ? Activities requests
import sigss_principal.requests.activity_requests as act_req

urlpatterns = [
    path("", principal, name="inicio"),
    path("inicio_sesion", inicio, name="inicio_sesion"),
    path("iniciar_sesion", iniciar_sesion, name="iniciar_sesion"),
    path("cerrar_sesion", cerrar, name="cerrar_sesion"),
    path("enviar", enviar_mensaje, name="enviar"),
    path("tarco", index, name="principal"),
    path("getInfo", informacion, name="informacion"),
    path("agregarItem", enviar_item, name="enviar_item"),
    path("actualizarItem", modificar_item, name="actualizar_item"),
    path("eliminarItem", eliminar_item, name="eliminar_item"),
    # ? General manteinment requests
    path("plataforma/general", general_view, name="principal"),
    # ? Activities requests
    path("plataforma/actividades", activities_view, name="actividades"),
    path("plataforma/actividades/crear_actividad", act_req.create_activity, name="crear_actividad"),
    path("activities/getActivities", act_req.create_activity, name="crear_actividad"),
    # ? Items requests
    path("plataforma/equipo", items_view, name="items"),
    # path("mantenimiento_preventivo", manteinment_1_view, name="manteinment1"),
    # ? Manteinment requests
    path("plataforma/mantenimiento_correctivo", manteinment_view, name="manteinment"),
]