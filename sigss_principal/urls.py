from django.urls import path

from sigss_principal.views import *


urlpatterns = [
    path("", principal, name="inicio"),
    path("enviar", enviar_mensaje, name="enviar")
]