from django.urls import path
from tarco_platform.views import *
# ? Importing Activities requests
import tarco_platform.requests.activity_requests as act_req
# ? Importing Items requests
import tarco_platform.requests.items_requests as it_req
# ? Importing General Manteinment requests
import tarco_platform.requests.general_requests as g_req
# ? Importing Corrective Manteinment requests
import tarco_platform.requests.manteinment_requests as mnt_req
# ? Importing Providers requests
import tarco_platform.requests.providers_requests as pro_req
# ? Importing Other requests
import tarco_platform.requests.frequences_requests as fec_req
import tarco_platform.requests.novelties_requests as nov_req
import tarco_platform.requests.modes_requests as mod_req
import tarco_platform.requests.state_mant_requests as st_req

urlpatterns = [
    path("", index, name="generalMantTARCO"),
    path("actividades", activities, name="activitiesTARCO"),
    path("equipos", items, name="itemsTARCO"),
    path("mantenimiento-correctivo", correc_manteinment, name="corMantTARCO"),
    path("otros-registros", other_views, name="otherRegistersTARCO"),

    # ? General manteinment requests
    path("operaciones_tarco/general/mostrarGeneral", g_req.show_general_mant, name="showGeneralMntTARCO"),
    path("operaciones_tarco/general/crearGeneral", g_req.create_general, name="createGeneralMntTARCO"),
    path("operaciones_tarco/general/modificarGeneral", g_req.modify_general, name="modifyGeneralMntTARCO"),
    path("operaciones_tarco/general/eliminarGeneral", g_req.delete_general, name="deleteGeneralMntTARCO"),
    # ? Activities requests
    path("operaciones_tarco/actividades/crear_actividad", act_req.create_activity, name="createActivityTARCO"),
    path("operaciones_tarco/actividades/modificarActividad", act_req.modify_activity, name="modifyActivityTARCO"),
    path("operaciones_tarco/actividades/mostrarActividad", act_req.show_activities, name="showAcivitiesTARCO"),
    path("operaciones_tarco/actividades/buscarActividad", act_req.search_activity, name="searchActivityTARCO"),
    path("operaciones_tarco/actividades/eliminarActividad", act_req.delete_activity, name="deleteActivityTARCO"),
    path("operaciones_tarco/actividades/eliminarActividadCompleto", act_req.delete_activity_with_mant, name="deleteAllActivityTARCO"),
    # ? Items requests
    path("operaciones_tarco/equipo/mostrarItems", it_req.show_items, name="showItemsTARCO"),
    path("operaciones_tarco/equipo/modificarItem", it_req.modify_item, name="modifyItemsTARCO"),
    path("operaciones_tarco/equipo/info_item/<slug:id_item>", item_view, name="itemTARCO"),
    path("operaciones_tarco/equipo/registrarItem", it_req.create_item, name="createItemTARCO"),
    path("operaciones_tarco/equipo/buscarItem", it_req.search_item, name="searchItemTARCO"),
    path("operaciones_tarco/equipo/eliminarItem", it_req.delete_item, name="deleteItemTARCO"),
    path("operaciones_tarco/equipo/eliminarItemCompleto", it_req.delete_item_complete, name="deleteCompleteItemTARCO"),
    path("operaciones_tarco/equipo/modificarCaracteristicas", it_req.modify_carateristics, name="modifyCaracteristicsTARCO"),
    # ? Manteinment requests
    path("operaciones_tarco/correctivo/mostrarCorrectivo", mnt_req.show_corrective_mant, name="showManteinmentsTARCO"),
    path("operaciones_tarco/correctivo/agregarCorrectivo", mnt_req.create_manteinment, name="createManteinmentTARCO"),
    path("operaciones_tarco/correctivo/modificarCorrectivo", mnt_req.modify_manteinment, name="modifyManteinmentTARCO"),
    path("operaciones_tarco/correctivo/eliminarCorrectivo", mnt_req.delete_manteinment, name="deleteManteinmentTARCO"),
    # ? Provider requests
    path("operaciones_tarco/proveedor/mostrarProveedores", pro_req.show_providers, name="showProvidersTARCO"),
    path("operaciones_tarco/proveedor/agregarProveedor", pro_req.create_provider, name="createProvidersTARCO"),
    path("operaciones_tarco/proveedor/agregarProveedorAItem", pro_req.add_provider_to_item, name="addProviderToItemTARCO"),
    path("operaciones_tarco/proveedor/modificarProveedor", pro_req.modify_provider, name="modifyProvidersTARCO"),
    path("operaciones_tarco/proveedor/eliminarProveedor", pro_req.delete_provider, name="deleteProvidersTARCO"),
    path("operaciones_tarco/proveedor/cambiarProveedor", pro_req.change_provider, name="changeProviderToItemTARCO"),
    path("operaciones_tarco/proveedor/buscarProveedor", pro_req.search_provider, name="searchProviderTARCO"),
    path("operaciones_tarco/proveedor/quitarProveedor", pro_req.delete_provider_from_item, name="removeProviderToItemTARCO"),
    # ? Other requests
    path("operaciones_tarco/estado/mostrarEstados", st_req.showStates, name="showStatesTARCO"),
    path("operaciones_tarco/estado/crearEstado", st_req.createState, name="createStateTARCO"),
    path("operaciones_tarco/estado/modificarEstado", st_req.modifyState, name="modifyStateTARCO"),
    path("operaciones_tarco/estado/eliminarEstado", st_req.deleteState, name="deleteStateTARCO"),
    path("operaciones_tarco/estado/buscarEstado", st_req.searchState, name="searchStateTARCO"),
    path("operaciones_tarco/frecuencia/mostrarFrecuencias", fec_req.showFrequences, name="showFrequencesTARCO"),
    path("operaciones_tarco/frecuencia/crearFrecuencia", fec_req.createFrequence, name="createFrequenceTARCO"),
    path("operaciones_tarco/frecuencia/modificarFrecuencia", fec_req.modifyFrequence, name="modifyFrequenceTARCO"),
    path("operaciones_tarco/frecuencia/eliminarFrecuencia", fec_req.deleteFrequence, name="deleteFrequenceTARCO"),
    path("operaciones_tarco/frecuencia/buscarFrecuencia", fec_req.searchFrequence, name="searchFrequenceTARCO"),
    path("operaciones_tarco/novedad/mostrarNovedades", nov_req.showNovelties, name="showNoveltiesTARCO"),
    path("operaciones_tarco/novedad/crearNovedad", nov_req.createNovelty, name="createNoveltyTARCO"),
    path("operaciones_tarco/novedad/modificarNovedad", nov_req.modifyNovelty, name="modifyNoveltyTARCO"),
    path("operaciones_tarco/novedad/eliminarNovedad", nov_req.deleteNovelty, name="deleteNoveltyTARCO"),
    path("operaciones_tarco/novedad/buscarNovedad", nov_req.searchNovelty, name="searchNoveltyTARCO"),
    path("operaciones_tarco/modoFallo/mostrarModos", mod_req.showModes, name="showModesTARCO"),
    path("operaciones_tarco/modoFallo/crearModo", mod_req.createMode, name="createModeTARCO"),
    path("operaciones_tarco/modoFallo/modificarModo", mod_req.modifyMode, name="modifyModeTARCO"),
    path("operaciones_tarco/modoFallo/eliminarModo", mod_req.deleteMode, name="deleteModeTARCO"),
    path("operaciones_tarco/modoFallo/buscarModo", mod_req.searchMode, name="searchModeTARCO"),
]