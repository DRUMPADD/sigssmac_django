from django.urls import path
from api_platform.views import *

# ? Importing Activities requests
import api_platform.requests.activity_requests as act_req
# ? Importing Items requests
import api_platform.requests.items_requests as it_req
# ? Importing General Manteinment requests
import api_platform.requests.general_requests as g_req
# ? Importing Corrective Manteinment requests
import api_platform.requests.manteinment_requests as mnt_req
# ? Importing Providers requests
import api_platform.requests.providers_requests as pro_req
# ? Importing Other requests
import api_platform.requests.frequences_requests as fec_req
import api_platform.requests.novelties_requests as nov_req
import api_platform.requests.modes_requests as mod_req
import api_platform.requests.state_mant_requests as st_req

urlpatterns = [
    path("", index, name="generalMantAPI"),
    path("actividades", activities, name="activitiesAPI"),
    path("equipos", items, name="itemsAPI"),
    path("mantenimiento-correctivo", correc_manteinment, name="corMantAPI"),
    path("otros-registros", other_views, name="otherRegistersAPI"),

    # ? General manteinment requests
    path("plataforma/general/mostrarGeneral", g_req.show_general_mant, name="showGeneralMnt"),
    path("plataforma/general/crearGeneral", g_req.create_general, name="createGeneralMnt"),
    path("plataforma/general/modificarGeneral", g_req.modify_general, name="modifyGeneralMnt"),
    path("plataforma/general/eliminarGeneral", g_req.delete_general, name="deleteGeneralMnt"),
    # ? Activities requests
    path("plataforma/actividades/crear_actividad", act_req.create_activity, name="createActivity"),
    path("plataforma/actividades/modificarActividad", act_req.modify_activity, name="modifyActivity"),
    path("plataforma/actividades/mostrarActividad", act_req.show_activities, name="showAcivities"),
    path("plataforma/actividades/buscarActividad", act_req.search_activity, name="searchActivity"),
    path("plataforma/actividades/eliminarActividad", act_req.delete_activity, name="deleteActivity"),
    path("plataforma/actividades/eliminarActividadCompleto", act_req.delete_activity_with_mant, name="deleteAllActivity"),
    # ? Items requests
    path("plataforma/equipo/mostrarItems", it_req.show_items, name="showItems"),
    path("plataforma/equipo/modificarItem", it_req.modify_item, name="modifyItems"),
    path("plataforma/equipo/info_item/<slug:id_item>", item_view, name="item"),
    path("plataforma/equipo/registrarItem", it_req.create_item, name="createItem"),
    path("plataforma/equipo/buscarItem", it_req.search_item, name="searchItem"),
    path("plataforma/equipo/eliminarItem", it_req.delete_item, name="deleteItem"),
    path("plataforma/equipo/eliminarItemCompleto", it_req.delete_item_complete, name="deleteCompleteItem"),
    path("plataforma/equipo/modificarCaracteristicas", it_req.modify_carateristics, name="modifyCaracteristics"),
    # ? Manteinment requests
    path("plataforma/correctivo/mostrarCorrectivo", mnt_req.show_corrective_mant, name="showManteinments"),
    path("plataforma/correctivo/agregarCorrectivo", mnt_req.create_manteinment, name="createManteinment"),
    path("plataforma/correctivo/modificarCorrectivo", mnt_req.modify_manteinment, name="modifyManteinment"),
    path("plataforma/correctivo/eliminarCorrectivo", mnt_req.delete_manteinment, name="deleteManteinment"),
    # ? Provider requests
    path("plataforma/proveedor/mostrarProveedores", pro_req.show_providers, name="showProviders"),
    path("plataforma/proveedor/agregarProveedor", pro_req.create_provider, name="createProviders"),
    path("plataforma/proveedor/agregarProveedorAItem", pro_req.add_provider_to_item, name="addProviderToItem"),
    path("plataforma/proveedor/modificarProveedor", pro_req.modify_provider, name="modifyProviders"),
    path("plataforma/proveedor/eliminarProveedor", pro_req.delete_provider, name="deleteProviders"),
    path("plataforma/proveedor/cambiarProveedor", pro_req.change_provider, name="changeProviderToItem"),
    path("plataforma/proveedor/buscarProveedor", pro_req.search_provider, name="searchProvider"),
    path("plataforma/proveedor/quitarProveedor", pro_req.delete_provider_from_item, name="removeProviderToItem"),
    # ? Other requests
    path("plataforma/otrosRegistros", other_views, name="other"),
    path("plataforma/estado/mostrarEstados", st_req.showStates, name="showStates"),
    path("plataforma/estado/crearEstado", st_req.createState, name="createState"),
    path("plataforma/estado/modificarEstado", st_req.modifyState, name="modifyState"),
    path("plataforma/estado/eliminarEstado", st_req.deleteState, name="deleteState"),
    path("plataforma/estado/buscarEstado", st_req.searchState, name="searchState"),
    path("plataforma/frecuencia/mostrarFrecuencias", fec_req.showFrequences, name="showFrequences"),
    path("plataforma/frecuencia/crearFrecuencia", fec_req.createFrequence, name="createFrequence"),
    path("plataforma/frecuencia/modificarFrecuencia", fec_req.modifyFrequence, name="modifyFrequence"),
    path("plataforma/frecuencia/eliminarFrecuencia", fec_req.deleteFrequence, name="deleteFrequence"),
    path("plataforma/frecuencia/buscarFrecuencia", fec_req.searchFrequence, name="searchFrequence"),
    path("plataforma/novedad/mostrarNovedades", nov_req.showNovelties, name="showNovelties"),
    path("plataforma/novedad/crearNovedad", nov_req.createNovelty, name="createNovelty"),
    path("plataforma/novedad/modificarNovedad", nov_req.modifyNovelty, name="modifyNovelty"),
    path("plataforma/novedad/eliminarNovedad", nov_req.deleteNovelty, name="deleteNovelty"),
    path("plataforma/novedad/buscarNovedad", nov_req.searchNovelty, name="searchNovelty"),
    path("plataforma/modoFallo/mostrarModos", mod_req.showModes, name="showModes"),
    path("plataforma/modoFallo/crearModo", mod_req.createMode, name="createMode"),
    path("plataforma/modoFallo/modificarModo", mod_req.modifyMode, name="modifyMode"),
    path("plataforma/modoFallo/eliminarModo", mod_req.deleteMode, name="deleteMode"),
    path("plataforma/modoFallo/buscarModo", mod_req.searchMode, name="searchMode"),
]