from django.urls import path

from .views import *
from sigss_principal.plataforma.views import *
# ? Importing Activities requests
import sigss_principal.plataforma.requests.activity_requests as act_req
# ? Importing Items requests
import sigss_principal.plataforma.requests.items_requests as it_req
# ? Importing General Manteinment requests
import sigss_principal.plataforma.requests.general_requests as g_req
# ? Importing Corrective Manteinment requests
import sigss_principal.plataforma.requests.manteinment_requests as mnt_req
# ? Importing Providers requests
import sigss_principal.plataforma.requests.providers_requests as pro_req

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
    path("plataforma/general/modificarGeneral", g_req.modify_general, name="modifyGeneralMnt"),
    path("plataforma/general/eliminarGeneral", g_req.delete_general, name="deleteGeneralMnt"),
    # ? Activities requests
    path("plataforma/actividades", activities_view, name="actividades"),
    path("plataforma/actividades/crear_actividad", act_req.create_activity, name="createActivity"),
    path("plataforma/actividades/modificarActividad", act_req.modify_activity, name="modifyActivity"),
    path("plataforma/actividades/mostrarActividad", act_req.show_activities, name="showAcivities"),
    path("plataforma/actividades/buscarActividad", act_req.search_activity, name="searchActivity"),
    path("plataforma/actividades/eliminarActividad", act_req.delete_activity, name="deleteActivity"),
    path("plataforma/actividades/eliminarActividadCompleto", act_req.delete_activity_with_mant, name="deleteAllActivity"),
    # ? Items requests
    path("plataforma/equipo", items_view, name="items"),
    path("plataforma/equipo/mostrarItems", it_req.show_items, name="showItems"),
    path("plataforma/equipo/modificarItem", it_req.modify_item, name="modifyItems"),
    path("plataforma/equipo/<slug:id_item>", item_view, name="item"),
    path("plataforma/equipo/registrarItem", it_req.create_item, name="createItem"),
    path("plataforma/equipo/buscarItem", it_req.search_item, name="searchItem"),
    # path("mantenimiento_preventivo", manteinment_1_view, name="manteinment1"),
    # ? Manteinment requests
    path("plataforma/mantenimiento_correctivo", manteinment_view, name="manteinment"),
    path("plataforma/correctivo/mostrarCorrectivo", mnt_req.show_corrective_mant, name="showManteinments"),
    # ? Provider requests
    path("plataforma/proveedor/mostrarProveedores", pro_req.show_providers, name="showProviders"),
    path("plataforma/correctivo/agregarProveedor", pro_req.create_provider, name="createProviders"),
    path("plataforma/correctivo/modificarProveedor", pro_req.modify_provider, name="modifyProviders"),
    path("plataforma/correctivo/eliminarProveedor", pro_req.delete_provider, name="deleteProviders"),
]