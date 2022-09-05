from django.urls import path

from .views import *
from sigss_principal.plataforma.views import *

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
    path("plataforma/general", general_view, name="principal"),
    path("plataforma/activitidades", activities_view, name="actividades"),
    path("plataforma/equipo", items_view, name="items"),
    # path("mantenimiento_preventivo", manteinment_1_view, name="manteinment1"),
    path("plataforma/mantenimiento_correctivo", manteinment_view, name="manteinment"),
]