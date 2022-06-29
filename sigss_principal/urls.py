from django.urls import path

from sigss_principal.views import *


urlpatterns = [
    path("", principal, name="inicio"),
    path("enviar", enviar_mensaje, name="enviar"),
    path("tarco", index, name="principal"),
    path("getInfo", informacion, name="informacion"),
    path("agregarItem", enviar_item, name="enviar_item"),
]