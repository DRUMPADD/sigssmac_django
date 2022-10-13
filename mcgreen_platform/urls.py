from django.urls import path
from mcgreen_platform.views import *
# ? Importing Activities requests
import mcgreen_platform.requests.activity_requests as act_req
# ? Importing Items requests
import mcgreen_platform.requests.items_requests as it_req
# ? Importing General Manteinment requests
import mcgreen_platform.requests.general_requests as g_req
# ? Importing Corrective Manteinment requests
import mcgreen_platform.requests.manteinment_requests as mnt_req
# ? Importing Providers requests
import mcgreen_platform.requests.providers_requests as pro_req
# ? Importing Other requests
import mcgreen_platform.requests.frequences_requests as fec_req
import mcgreen_platform.requests.novelties_requests as nov_req
import mcgreen_platform.requests.modes_requests as mod_req
import mcgreen_platform.requests.state_mant_requests as st_req

urlpatterns = [
    path("", index, name="generalMantMCGREEN"),
    path("actividades", activities, name="activitiesMCGREEN"),
    path("equipos", items, name="itemsMCGREEN"),
    path("mantenimiento-correctivo", correc_manteinment, name="corMantMCGREEN"),
    path("otros-registros", other_view, name="otherRegistersMCGREEN"),

    # ? General manteinment requests
    path("operaciones_mcgreen/general/mostrarGeneral", g_req.show_general_mant, name="showGeneralMntMCGREEN"),
    path("operaciones_mcgreen/general/crearGeneral", g_req.create_general, name="createGeneralMntMCGREEN"),
    path("operaciones_mcgreen/general/modificarGeneral", g_req.modify_general, name="modifyGeneralMntMCGREEN"),
    path("operaciones_mcgreen/general/eliminarGeneral", g_req.delete_general, name="deleteGeneralMntMCGREEN"),
    # ? Activities requests
    path("operaciones_mcgreen/actividades/crear_actividad", act_req.create_activity, name="createActivityMCGREEN"),
    path("operaciones_mcgreen/actividades/modificarActividad", act_req.modify_activity, name="modifyActivityMCGREEN"),
    path("operaciones_mcgreen/actividades/mostrarActividad", act_req.show_activities, name="showAcivitiesMCGREEN"),
    path("operaciones_mcgreen/actividades/buscarActividad", act_req.search_activity, name="searchActivityMCGREEN"),
    path("operaciones_mcgreen/actividades/eliminarActividad", act_req.delete_activity, name="deleteActivityMCGREEN"),
    path("operaciones_mcgreen/actividades/eliminarActividadCompleto", act_req.delete_activity_with_mant, name="deleteAllActivityMCGREEN"),
    # ? Items requests
    path("operaciones_mcgreen/equipo/mostrarItems", it_req.show_items, name="showItemsMCGREEN"),
    path("operaciones_mcgreen/equipo/modificarItem", it_req.modify_item, name="modifyItemsMCGREEN"),
    path("operaciones_mcgreen/equipo/info_item/<slug:id_item>", item_view, name="itemMCGREEN"),
    path("operaciones_mcgreen/equipo/registrarItem", it_req.create_item, name="createItemMCGREEN"),
    path("operaciones_mcgreen/equipo/buscarItem", it_req.search_item, name="searchItemMCGREEN"),
    path("operaciones_mcgreen/equipo/eliminarItem", it_req.delete_item, name="deleteItemMCGREEN"),
    path("operaciones_mcgreen/equipo/eliminarItemCompleto", it_req.delete_item_complete, name="deleteCompleteItemMCGREEN"),
    path("operaciones_mcgreen/equipo/modificarCaracteristicas", it_req.modify_carateristics, name="modifyCaracteristicsMCGREEN"),
    # ? Manteinment requests
    path("operaciones_mcgreen/correctivo/mostrarCorrectivo", mnt_req.show_corrective_mant, name="showManteinmentsMCGREEN"),
    path("operaciones_mcgreen/correctivo/agregarCorrectivo", mnt_req.create_manteinment, name="createManteinmentMCGREEN"),
    path("operaciones_mcgreen/correctivo/modificarCorrectivo", mnt_req.modify_manteinment, name="modifyManteinmentMCGREEN"),
    path("operaciones_mcgreen/correctivo/eliminarCorrectivo", mnt_req.delete_manteinment, name="deleteManteinmentMCGREEN"),
    # ? Provider requests
    path("operaciones_mcgreen/proveedor/mostrarProveedores", pro_req.show_providers, name="showProvidersMCGREEN"),
    path("operaciones_mcgreen/proveedor/agregarProveedor", pro_req.create_provider, name="createProvidersMCGREEN"),
    path("operaciones_mcgreen/proveedor/agregarProveedorAItem", pro_req.add_provider_to_item, name="addProviderToItemMCGREEN"),
    path("operaciones_mcgreen/proveedor/modificarProveedor", pro_req.modify_provider, name="modifyProvidersMCGREEN"),
    path("operaciones_mcgreen/proveedor/eliminarProveedor", pro_req.delete_provider, name="deleteProvidersMCGREEN"),
    path("operaciones_mcgreen/proveedor/cambiarProveedor", pro_req.change_provider, name="changeProviderToItemMCGREEN"),
    path("operaciones_mcgreen/proveedor/buscarProveedor", pro_req.search_provider, name="searchProviderMCGREEN"),
    path("operaciones_mcgreen/proveedor/quitarProveedor", pro_req.delete_provider_from_item, name="removeProviderToItemMCGREEN"),
    # ? Other requests
    path("operaciones_mcgreen/estado/mostrarEstados", st_req.showStates, name="showStatesMCGREEN"),
    path("operaciones_mcgreen/estado/crearEstado", st_req.createState, name="createStateMCGREEN"),
    path("operaciones_mcgreen/estado/modificarEstado", st_req.modifyState, name="modifyStateMCGREEN"),
    path("operaciones_mcgreen/estado/eliminarEstado", st_req.deleteState, name="deleteStateMCGREEN"),
    path("operaciones_mcgreen/estado/buscarEstado", st_req.searchState, name="searchStateMCGREEN"),
    path("operaciones_mcgreen/frecuencia/mostrarFrecuencias", fec_req.showFrequences, name="showFrequencesMCGREEN"),
    path("operaciones_mcgreen/frecuencia/crearFrecuencia", fec_req.createFrequence, name="createFrequenceMCGREEN"),
    path("operaciones_mcgreen/frecuencia/modificarFrecuencia", fec_req.modifyFrequence, name="modifyFrequenceMCGREEN"),
    path("operaciones_mcgreen/frecuencia/eliminarFrecuencia", fec_req.deleteFrequence, name="deleteFrequenceMCGREEN"),
    path("operaciones_mcgreen/frecuencia/buscarFrecuencia", fec_req.searchFrequence, name="searchFrequenceMCGREEN"),
    path("operaciones_mcgreen/novedad/mostrarNovedades", nov_req.showNovelties, name="showNoveltiesMCGREEN"),
    path("operaciones_mcgreen/novedad/crearNovedad", nov_req.createNovelty, name="createNoveltyMCGREEN"),
    path("operaciones_mcgreen/novedad/modificarNovedad", nov_req.modifyNovelty, name="modifyNoveltyMCGREEN"),
    path("operaciones_mcgreen/novedad/eliminarNovedad", nov_req.deleteNovelty, name="deleteNoveltyMCGREEN"),
    path("operaciones_mcgreen/novedad/buscarNovedad", nov_req.searchNovelty, name="searchNoveltyMCGREEN"),
    path("operaciones_mcgreen/modoFallo/mostrarModos", mod_req.showModes, name="showModesMCGREEN"),
    path("operaciones_mcgreen/modoFallo/crearModo", mod_req.createMode, name="createModeMCGREEN"),
    path("operaciones_mcgreen/modoFallo/modificarModo", mod_req.modifyMode, name="modifyModeMCGREEN"),
    path("operaciones_mcgreen/modoFallo/eliminarModo", mod_req.deleteMode, name="deleteModeMCGREEN"),
    path("operaciones_mcgreen/modoFallo/buscarModo", mod_req.searchMode, name="searchModeMCGREEN"),
]