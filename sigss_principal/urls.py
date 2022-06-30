from django.urls import path

from sigss_principal.views import *


urlpatterns = [
    path("", principal, name="inicio"),
    path("enviar", enviar_mensaje, name="enviar"),
    path("tarco", index, name="principal"),
    path("getInfo", informacion, name="informacion"),
    path("agregarItem", enviar_item, name="enviar_item"),
    path("actualizarItem", modificar_item, name="actualizar_item"),
    path("eliminarItem", eliminar_item, name="eliminar_item"),
]