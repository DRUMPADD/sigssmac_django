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
    path("operaciones_tarco/general/mostrarGeneral", g_req.show_general_mant, name="showGeneralMnt"),
    path("operaciones_tarco/general/crearGeneral", g_req.create_general, name="createGeneralMnt"),
    path("operaciones_tarco/general/modificarGeneral", g_req.modify_general, name="modifyGeneralMnt"),
    path("operaciones_tarco/general/eliminarGeneral", g_req.delete_general, name="deleteGeneralMnt"),
    # ? Activities requests
    path("operaciones_tarco/actividades/crear_actividad", act_req.create_activity, name="createActivity"),
    path("operaciones_tarco/actividades/modificarActividad", act_req.modify_activity, name="modifyActivity"),
    path("operaciones_tarco/actividades/mostrarActividad", act_req.show_activities, name="showAcivities"),
    path("operaciones_tarco/actividades/buscarActividad", act_req.search_activity, name="searchActivity"),
    path("operaciones_tarco/actividades/eliminarActividad", act_req.delete_activity, name="deleteActivity"),
    path("operaciones_tarco/actividades/eliminarActividadCompleto", act_req.delete_activity_with_mant, name="deleteAllActivity"),
    # ? Items requests
    path("operaciones_tarco/equipo/mostrarItems", it_req.show_items, name="showItems"),
    path("operaciones_tarco/equipo/modificarItem", it_req.modify_item, name="modifyItems"),
    path("operaciones_tarco/equipo/info_item/<slug:id_item>", item_view, name="item"),
    path("operaciones_tarco/equipo/registrarItem", it_req.create_item, name="createItem"),
    path("operaciones_tarco/equipo/buscarItem", it_req.search_item, name="searchItem"),
    path("operaciones_tarco/equipo/eliminarItem", it_req.delete_item, name="deleteItem"),
    path("operaciones_tarco/equipo/eliminarItemCompleto", it_req.delete_item_complete, name="deleteCompleteItem"),
    path("operaciones_tarco/equipo/modificarCaracteristicas", it_req.modify_carateristics, name="modifyCaracteristics"),
    # ? Manteinment requests
    path("operaciones_tarco/correctivo/mostrarCorrectivo", mnt_req.show_corrective_mant, name="showManteinments"),
    path("operaciones_tarco/correctivo/agregarCorrectivo", mnt_req.create_manteinment, name="createManteinment"),
    path("operaciones_tarco/correctivo/modificarCorrectivo", mnt_req.modify_manteinment, name="modifyManteinment"),
    path("operaciones_tarco/correctivo/eliminarCorrectivo", mnt_req.delete_manteinment, name="deleteManteinment"),
    # ? Provider requests
    path("operaciones_tarco/proveedor/mostrarProveedores", pro_req.show_providers, name="showProviders"),
    path("operaciones_tarco/proveedor/agregarProveedor", pro_req.create_provider, name="createProviders"),
    path("operaciones_tarco/proveedor/agregarProveedorAItem", pro_req.add_provider_to_item, name="addProviderToItem"),
    path("operaciones_tarco/proveedor/modificarProveedor", pro_req.modify_provider, name="modifyProviders"),
    path("operaciones_tarco/proveedor/eliminarProveedor", pro_req.delete_provider, name="deleteProviders"),
    path("operaciones_tarco/proveedor/cambiarProveedor", pro_req.change_provider, name="changeProviderToItem"),
    path("operaciones_tarco/proveedor/buscarProveedor", pro_req.search_provider, name="searchProvider"),
    path("operaciones_tarco/proveedor/quitarProveedor", pro_req.delete_provider_from_item, name="removeProviderToItem"),
    # ? Other requests
    path("operaciones_tarco/otrosRegistros", other_view, name="other"),
    path("operaciones_tarco/estado/mostrarEstados", st_req.showStates, name="showStates"),
    path("operaciones_tarco/estado/crearEstado", st_req.createState, name="createState"),
    path("operaciones_tarco/estado/modificarEstado", st_req.modifyState, name="modifyState"),
    path("operaciones_tarco/estado/eliminarEstado", st_req.deleteState, name="deleteState"),
    path("operaciones_tarco/estado/buscarEstado", st_req.searchState, name="searchState"),
    path("operaciones_tarco/frecuencia/mostrarFrecuencias", fec_req.showFrequences, name="showFrequences"),
    path("operaciones_tarco/frecuencia/crearFrecuencia", fec_req.createFrequence, name="createFrequence"),
    path("operaciones_tarco/frecuencia/modificarFrecuencia", fec_req.modifyFrequence, name="modifyFrequence"),
    path("operaciones_tarco/frecuencia/eliminarFrecuencia", fec_req.deleteFrequence, name="deleteFrequence"),
    path("operaciones_tarco/frecuencia/buscarFrecuencia", fec_req.searchFrequence, name="searchFrequence"),
    path("operaciones_tarco/novedad/mostrarNovedades", nov_req.showNovelties, name="showNovelties"),
    path("operaciones_tarco/novedad/crearNovedad", nov_req.createNovelty, name="createNovelty"),
    path("operaciones_tarco/novedad/modificarNovedad", nov_req.modifyNovelty, name="modifyNovelty"),
    path("operaciones_tarco/novedad/eliminarNovedad", nov_req.deleteNovelty, name="deleteNovelty"),
    path("operaciones_tarco/novedad/buscarNovedad", nov_req.searchNovelty, name="searchNovelty"),
    path("operaciones_tarco/modoFallo/mostrarModos", mod_req.showModes, name="showModes"),
    path("operaciones_tarco/modoFallo/crearModo", mod_req.createMode, name="createMode"),
    path("operaciones_tarco/modoFallo/modificarModo", mod_req.modifyMode, name="modifyMode"),
    path("operaciones_tarco/modoFallo/eliminarModo", mod_req.deleteMode, name="deleteMode"),
    path("operaciones_tarco/modoFallo/buscarModo", mod_req.searchMode, name="searchMode"),
]