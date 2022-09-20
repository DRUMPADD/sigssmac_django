from django.urls import path

from .views import *
from sigss_principal.plataforma.views import *
# ? Importing Activities requests
import sigss_principal.plataforma.requests.activity_requests as act_req
# ? Importing Items requests
import sigss_principal.plataforma.requests.items_requests as it_req
# ? Importing General Manteinment requests
import sigss_principal.plataforma.requests.general_requests as g_req

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
    path("plataforma/general/mostrarGeneral", g_req.show_general_mant, name="showGeneralMnt"),
    path("plataforma/general/crearGeneral", g_req.create_general, name="createGeneralMnt"),
    # ? Activities requests
    path("plataforma/actividades", activities_view, name="actividades"),
    path("plataforma/actividades/crear_actividad", act_req.create_activity, name="createActivity"),
    path("plataforma/actividades/modificarActividad", act_req.modify_activity, name="modifyActivity"),
    path("plataforma/actividades/motrarActividad", act_req.show_activities, name="showAcivities"),
    # ? Items requests
    path("plataforma/equipo", items_view, name="items"),
    path("plataforma/equipo/mostrarItems", it_req.show_items, name="showItems"),
    path("plataforma/equipo/modificarItem", it_req.modify_item, name="modifyItems"),
    path("plataforma/equipo/<slug:id_item>", item_view, name="item"),
    path("plataforma/equipo/registrarItem", it_req.create_item, name="createItem"),
    # path("mantenimiento_preventivo", manteinment_1_view, name="manteinment1"),
    # ? Manteinment requests
    path("plataforma/mantenimiento_correctivo", manteinment_view, name="manteinment"),
]