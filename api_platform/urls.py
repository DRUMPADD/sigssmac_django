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
    path("operaciones_api/general/mostrarGeneral", g_req.show_general_mant, name="showGeneralMntAPI"),
    path("operaciones_api/general/crearGeneral", g_req.create_general, name="createGeneralMntAPI"),
    path("operaciones_api/general/modificarGeneral", g_req.modify_general, name="modifyGeneralMntAPI"),
    path("operaciones_api/general/eliminarGeneral", g_req.delete_general, name="deleteGeneralMntAPI"),
    # ? Activities requests
    path("operaciones_api/actividades/crear_actividad", act_req.create_activity, name="createActivityAPI"),
    path("operaciones_api/actividades/modificarActividad", act_req.modify_activity, name="modifyActivityAPI"),
    path("operaciones_api/actividades/mostrarActividad", act_req.show_activities, name="showAcivitiesAPI"),
    path("operaciones_api/actividades/buscarActividad", act_req.search_activity, name="searchActivityAPI"),
    path("operaciones_api/actividades/eliminarActividad", act_req.delete_activity, name="deleteActivityAPI"),
    path("operaciones_api/actividades/eliminarActividadCompleto", act_req.delete_activity_with_mant, name="deleteAllActivityAPI"),
    # ? Items requests
    path("operaciones_api/equipo/mostrarItems", it_req.show_items, name="showItemsAPI"),
    path("operaciones_api/equipo/modificarItem", it_req.modify_item, name="modifyItemsAPI"),
    path("operaciones_api/equipo/info_item/<slug:id_item>", item_view, name="itemAPI"),
    path("operaciones_api/equipo/registrarItem", it_req.create_item, name="createItemAPI"),
    path("operaciones_api/equipo/buscarItem", it_req.search_item, name="searchItemAPI"),
    path("operaciones_api/equipo/eliminarItem", it_req.delete_item, name="deleteItemAPI"),
    path("operaciones_api/equipo/eliminarItemCompleto", it_req.delete_item_complete, name="deleteCompleteItemAPI"),
    path("operaciones_api/equipo/modificarCaracteristicas", it_req.modify_carateristics, name="modifyCaracteristicsAPI"),
    # ? Manteinment requests
    path("operaciones_api/correctivo/mostrarCorrectivo", mnt_req.show_corrective_mant, name="showManteinmentsAPI"),
    path("operaciones_api/correctivo/agregarCorrectivo", mnt_req.create_manteinment, name="createManteinmentAPI"),
    path("operaciones_api/correctivo/modificarCorrectivo", mnt_req.modify_manteinment, name="modifyManteinmentAPI"),
    path("operaciones_api/correctivo/eliminarCorrectivo", mnt_req.delete_manteinment, name="deleteManteinmentAPI"),
    # ? Provider requests
    path("operaciones_api/proveedor/mostrarProveedores", pro_req.show_providers, name="showProvidersAPI"),
    path("operaciones_api/proveedor/agregarProveedor", pro_req.create_provider, name="createProvidersAPI"),
    path("operaciones_api/proveedor/agregarProveedorAItem", pro_req.add_provider_to_item, name="addProviderToItemAPI"),
    path("operaciones_api/proveedor/modificarProveedor", pro_req.modify_provider, name="modifyProvidersAPI"),
    path("operaciones_api/proveedor/eliminarProveedor", pro_req.delete_provider, name="deleteProvidersAPI"),
    path("operaciones_api/proveedor/cambiarProveedor", pro_req.change_provider, name="changeProviderToItemAPI"),
    path("operaciones_api/proveedor/buscarProveedor", pro_req.search_provider, name="searchProviderAPI"),
    path("operaciones_api/proveedor/quitarProveedor", pro_req.delete_provider_from_item, name="removeProviderToItemAPI"),
    # ? Other requests
    path("operaciones_api/estado/mostrarEstados", st_req.showStates, name="showStatesAPI"),
    path("operaciones_api/estado/crearEstado", st_req.createState, name="createStateAPI"),
    path("operaciones_api/estado/modificarEstado", st_req.modifyState, name="modifyStateAPI"),
    path("operaciones_api/estado/eliminarEstado", st_req.deleteState, name="deleteStateAPI"),
    path("operaciones_api/estado/buscarEstado", st_req.searchState, name="searchStateAPI"),
    path("operaciones_api/frecuencia/mostrarFrecuencias", fec_req.showFrequences, name="showFrequencesAPI"),
    path("operaciones_api/frecuencia/crearFrecuencia", fec_req.createFrequence, name="createFrequenceAPI"),
    path("operaciones_api/frecuencia/modificarFrecuencia", fec_req.modifyFrequence, name="modifyFrequenceAPI"),
    path("operaciones_api/frecuencia/eliminarFrecuencia", fec_req.deleteFrequence, name="deleteFrequenceAPI"),
    path("operaciones_api/frecuencia/buscarFrecuencia", fec_req.searchFrequence, name="searchFrequenceAPI"),
    path("operaciones_api/novedad/mostrarNovedades", nov_req.showNovelties, name="showNoveltiesAPI"),
    path("operaciones_api/novedad/crearNovedad", nov_req.createNovelty, name="createNoveltyAPI"),
    path("operaciones_api/novedad/modificarNovedad", nov_req.modifyNovelty, name="modifyNoveltyAPI"),
    path("operaciones_api/novedad/eliminarNovedad", nov_req.deleteNovelty, name="deleteNoveltyAPI"),
    path("operaciones_api/novedad/buscarNovedad", nov_req.searchNovelty, name="searchNoveltyAPI"),
    path("operaciones_api/modoFallo/mostrarModos", mod_req.showModes, name="showModesAPI"),
    path("operaciones_api/modoFallo/crearModo", mod_req.createMode, name="createModeAPI"),
    path("operaciones_api/modoFallo/modificarModo", mod_req.modifyMode, name="modifyModeAPI"),
    path("operaciones_api/modoFallo/eliminarModo", mod_req.deleteMode, name="deleteModeAPI"),
    path("operaciones_api/modoFallo/buscarModo", mod_req.searchMode, name="searchModeAPI"),
]