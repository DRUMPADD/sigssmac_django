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
    path("operaciones_api/general/mostrarGeneral", g_req.show_general_mant, name="showGeneralMnt"),
    path("operaciones_api/general/crearGeneral", g_req.create_general, name="createGeneralMnt"),
    path("operaciones_api/general/modificarGeneral", g_req.modify_general, name="modifyGeneralMnt"),
    path("operaciones_api/general/eliminarGeneral", g_req.delete_general, name="deleteGeneralMnt"),
    # ? Activities requests
    path("operaciones_api/actividades/crear_actividad", act_req.create_activity, name="createActivity"),
    path("operaciones_api/actividades/modificarActividad", act_req.modify_activity, name="modifyActivity"),
    path("operaciones_api/actividades/mostrarActividad", act_req.show_activities, name="showAcivities"),
    path("operaciones_api/actividades/buscarActividad", act_req.search_activity, name="searchActivity"),
    path("operaciones_api/actividades/eliminarActividad", act_req.delete_activity, name="deleteActivity"),
    path("operaciones_api/actividades/eliminarActividadCompleto", act_req.delete_activity_with_mant, name="deleteAllActivity"),
    # ? Items requests
    path("operaciones_api/equipo/mostrarItems", it_req.show_items, name="showItems"),
    path("operaciones_api/equipo/modificarItem", it_req.modify_item, name="modifyItems"),
    path("operaciones_api/equipo/info_item/<slug:id_item>", item_view, name="item"),
    path("operaciones_api/equipo/registrarItem", it_req.create_item, name="createItem"),
    path("operaciones_api/equipo/buscarItem", it_req.search_item, name="searchItem"),
    path("operaciones_api/equipo/eliminarItem", it_req.delete_item, name="deleteItem"),
    path("operaciones_api/equipo/eliminarItemCompleto", it_req.delete_item_complete, name="deleteCompleteItem"),
    path("operaciones_api/equipo/modificarCaracteristicas", it_req.modify_carateristics, name="modifyCaracteristics"),
    # ? Manteinment requests
    path("operaciones_api/correctivo/mostrarCorrectivo", mnt_req.show_corrective_mant, name="showManteinments"),
    path("operaciones_api/correctivo/agregarCorrectivo", mnt_req.create_manteinment, name="createManteinment"),
    path("operaciones_api/correctivo/modificarCorrectivo", mnt_req.modify_manteinment, name="modifyManteinment"),
    path("operaciones_api/correctivo/eliminarCorrectivo", mnt_req.delete_manteinment, name="deleteManteinment"),
    # ? Provider requests
    path("operaciones_api/proveedor/mostrarProveedores", pro_req.show_providers, name="showProviders"),
    path("operaciones_api/proveedor/agregarProveedor", pro_req.create_provider, name="createProviders"),
    path("operaciones_api/proveedor/agregarProveedorAItem", pro_req.add_provider_to_item, name="addProviderToItem"),
    path("operaciones_api/proveedor/modificarProveedor", pro_req.modify_provider, name="modifyProviders"),
    path("operaciones_api/proveedor/eliminarProveedor", pro_req.delete_provider, name="deleteProviders"),
    path("operaciones_api/proveedor/cambiarProveedor", pro_req.change_provider, name="changeProviderToItem"),
    path("operaciones_api/proveedor/buscarProveedor", pro_req.search_provider, name="searchProvider"),
    path("operaciones_api/proveedor/quitarProveedor", pro_req.delete_provider_from_item, name="removeProviderToItem"),
    # ? Other requests
    path("operaciones_api/estado/mostrarEstados", st_req.showStates, name="showStates"),
    path("operaciones_api/estado/crearEstado", st_req.createState, name="createState"),
    path("operaciones_api/estado/modificarEstado", st_req.modifyState, name="modifyState"),
    path("operaciones_api/estado/eliminarEstado", st_req.deleteState, name="deleteState"),
    path("operaciones_api/estado/buscarEstado", st_req.searchState, name="searchState"),
    path("operaciones_api/frecuencia/mostrarFrecuencias", fec_req.showFrequences, name="showFrequences"),
    path("operaciones_api/frecuencia/crearFrecuencia", fec_req.createFrequence, name="createFrequence"),
    path("operaciones_api/frecuencia/modificarFrecuencia", fec_req.modifyFrequence, name="modifyFrequence"),
    path("operaciones_api/frecuencia/eliminarFrecuencia", fec_req.deleteFrequence, name="deleteFrequence"),
    path("operaciones_api/frecuencia/buscarFrecuencia", fec_req.searchFrequence, name="searchFrequence"),
    path("operaciones_api/novedad/mostrarNovedades", nov_req.showNovelties, name="showNovelties"),
    path("operaciones_api/novedad/crearNovedad", nov_req.createNovelty, name="createNovelty"),
    path("operaciones_api/novedad/modificarNovedad", nov_req.modifyNovelty, name="modifyNovelty"),
    path("operaciones_api/novedad/eliminarNovedad", nov_req.deleteNovelty, name="deleteNovelty"),
    path("operaciones_api/novedad/buscarNovedad", nov_req.searchNovelty, name="searchNovelty"),
    path("operaciones_api/modoFallo/mostrarModos", mod_req.showModes, name="showModes"),
    path("operaciones_api/modoFallo/crearModo", mod_req.createMode, name="createMode"),
    path("operaciones_api/modoFallo/modificarModo", mod_req.modifyMode, name="modifyMode"),
    path("operaciones_api/modoFallo/eliminarModo", mod_req.deleteMode, name="deleteMode"),
    path("operaciones_api/modoFallo/buscarModo", mod_req.searchMode, name="searchMode"),
]