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
# ? Importing Other requests
import sigss_principal.plataforma.requests.frequences_requests as fec_req
import sigss_principal.plataforma.requests.novelties_requests as nov_req
import sigss_principal.plataforma.requests.modes_requests as mod_req
import sigss_principal.plataforma.requests.state_mant_requests as st_req

# ? Importing Activities requests
import api_platform.requests.activity_requests as api_act_req
# ? Importing Items requests
import api_platform.requests.items_requests as api_it_req
# ? Importing General Manteinment requests
import api_platform.requests.general_requests as api_g_req
# ? Importing Corrective Manteinment requests
import api_platform.requests.manteinment_requests as api_mnt_req
# ? Importing Providers requests
import api_platform.requests.providers_requests as api_pro_req
# ? Importing Other requests
import api_platform.requests.frequences_requests as api_fec_req
import api_platform.requests.novelties_requests as api_nov_req
import api_platform.requests.modes_requests as api_mod_req
import api_platform.requests.state_mant_requests as api_st_req
import api_platform.views as api_acc_v
import api_platform.accidents as api_acc

# ? Importing Activities requests
import mcgreen_platform.requests.activity_requests as mcgreen_act_req
# ? Importing Items requests
import mcgreen_platform.requests.items_requests as mcgreen_it_req
# ? Importing General Manteinment requests
import mcgreen_platform.requests.general_requests as mcgreen_g_req
# ? Importing Corrective Manteinment requests
import mcgreen_platform.requests.manteinment_requests as mcgreen_mnt_req
# ? Importing Providers requests
import mcgreen_platform.requests.providers_requests as mcgreen_pro_req
# ? Importing Other requests
import mcgreen_platform.requests.frequences_requests as mcgreen_fec_req
import mcgreen_platform.requests.novelties_requests as mcgreen_nov_req
import mcgreen_platform.requests.modes_requests as mcgreen_mod_req
import mcgreen_platform.requests.state_mant_requests as mcgreen_st_req
import mcgreen_platform.views as mcgreen_acc_v
import mcgreen_platform.accidents as mcgreen_acc

# ? Importing Activities requests
import tarco_platform.requests.activity_requests as tarco_act_req
# ? Importing Items requests
import tarco_platform.requests.items_requests as tarco_it_req
# ? Importing General Manteinment requests
import tarco_platform.requests.general_requests as tarco_g_req
# ? Importing Corrective Manteinment requests
import tarco_platform.requests.manteinment_requests as tarco_mnt_req
# ? Importing Providers requests
import tarco_platform.requests.providers_requests as tarco_pro_req
# ? Importing Other requests
import tarco_platform.requests.frequences_requests as tarco_fec_req
import tarco_platform.requests.novelties_requests as tarco_nov_req
import tarco_platform.requests.modes_requests as tarco_mod_req
import tarco_platform.requests.state_mant_requests as tarco_st_req
import tarco_platform.views as tarco_acc_v
import tarco_platform.accidents as tarco_acc

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
    path("plataforma/equipo/info_item/<slug:id_item>", item_view, name="item"),
    path("plataforma/equipo/registrarItem", it_req.create_item, name="createItem"),
    path("plataforma/equipo/buscarItem", it_req.search_item, name="searchItem"),
    path("plataforma/equipo/eliminarItem", it_req.delete_item, name="deleteItem"),
    path("plataforma/equipo/eliminarItemCompleto", it_req.delete_item_complete, name="deleteCompleteItem"),
    path("plataforma/equipo/modificarCaracteristicas", it_req.modify_carateristics, name="modifyCaracteristics"),
    # path("mantenimiento_preventivo", manteinment_1_view, name="manteinment1"),
    # ? Manteinment requests
    path("plataforma/mantenimiento_correctivo", manteinment_view, name="manteinment"),
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
    path("plataforma/otrosRegistros", other_view, name="other"),
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


    # ?? API ENERGY - All requests
    # ? General manteinment requests
    path("operaciones_api/general/mostrarGeneral", api_g_req.show_general_mant, name="showGeneralMntAPI"),
    path("operaciones_api/general/crearGeneral", api_g_req.create_general, name="createGeneralMntAPI"),
    path("operaciones_api/general/modificarGeneral", api_g_req.modify_general, name="modifyGeneralMntAPI"),
    path("operaciones_api/general/eliminarGeneral", api_g_req.delete_general, name="deleteGeneralMntAPI"),
    # ? Activities requests
    path("operaciones_api/actividades/crear_actividad", api_act_req.create_activity, name="createActivityAPI"),
    path("operaciones_api/actividades/modificarActividad", api_act_req.modify_activity, name="modifyActivityAPI"),
    path("operaciones_api/actividades/mostrarActividad", api_act_req.show_activities, name="showAcivitiesAPI"),
    path("operaciones_api/actividades/buscarActividad", api_act_req.search_activity, name="searchActivityAPI"),
    path("operaciones_api/actividades/eliminarActividad", api_act_req.delete_activity, name="deleteActivityAPI"),
    path("operaciones_api/actividades/eliminarActividadCompleto", api_act_req.delete_activity_with_mant, name="deleteAllActivityAPI"),
    # ? Items requests
    path("operaciones_api/equipo/mostrarItems", api_it_req.show_items, name="showItemsAPI"),
    path("operaciones_api/equipo/modificarItem", api_it_req.modify_item, name="modifyItemsAPI"),
    path("operaciones_api/equipo/info_item/<slug:id_item>", item_view, name="itemAPI"),
    path("operaciones_api/equipo/registrarItem", api_it_req.create_item, name="createItemAPI"),
    path("operaciones_api/equipo/buscarItem", api_it_req.search_item, name="searchItemAPI"),
    path("operaciones_api/equipo/eliminarItem", api_it_req.delete_item, name="deleteItemAPI"),
    path("operaciones_api/equipo/eliminarItemCompleto", api_it_req.delete_item_complete, name="deleteCompleteItemAPI"),
    path("operaciones_api/equipo/modificarCaracteristicas", api_it_req.modify_carateristics, name="modifyCaracteristicsAPI"),
    # ? Manteinment requests
    path("operaciones_api/correctivo/mostrarCorrectivo", api_mnt_req.show_corrective_mant, name="showManteinmentsAPI"),
    path("operaciones_api/correctivo/agregarCorrectivo", api_mnt_req.create_manteinment, name="createManteinmentAPI"),
    path("operaciones_api/correctivo/modificarCorrectivo", api_mnt_req.modify_manteinment, name="modifyManteinmentAPI"),
    path("operaciones_api/correctivo/eliminarCorrectivo", api_mnt_req.delete_manteinment, name="deleteManteinmentAPI"),
    # ? Provider requests
    path("operaciones_api/proveedor/mostrarProveedores", api_pro_req.show_providers, name="showProvidersAPI"),
    path("operaciones_api/proveedor/agregarProveedor", api_pro_req.create_provider, name="createProvidersAPI"),
    path("operaciones_api/proveedor/agregarProveedorAItem", api_pro_req.add_provider_to_item, name="addProviderToItemAPI"),
    path("operaciones_api/proveedor/modificarProveedor", api_pro_req.modify_provider, name="modifyProvidersAPI"),
    path("operaciones_api/proveedor/eliminarProveedor", api_pro_req.delete_provider, name="deleteProvidersAPI"),
    path("operaciones_api/proveedor/cambiarProveedor", api_pro_req.change_provider, name="changeProviderToItemAPI"),
    path("operaciones_api/proveedor/buscarProveedor", api_pro_req.search_provider, name="searchProviderAPI"),
    path("operaciones_api/proveedor/quitarProveedor", api_pro_req.delete_provider_from_item, name="removeProviderToItemAPI"),
    # ? Other requests
    path("operaciones_api/estado/mostrarEstados", api_st_req.showStates, name="showStatesAPI"),
    path("operaciones_api/estado/crearEstado", api_st_req.createState, name="createStateAPI"),
    path("operaciones_api/estado/modificarEstado", api_st_req.modifyState, name="modifyStateAPI"),
    path("operaciones_api/estado/eliminarEstado", api_st_req.deleteState, name="deleteStateAPI"),
    path("operaciones_api/estado/buscarEstado", api_st_req.searchState, name="searchStateAPI"),
    path("operaciones_api/frecuencia/mostrarFrecuencias", api_fec_req.showFrequences, name="showFrequencesAPI"),
    path("operaciones_api/frecuencia/crearFrecuencia", api_fec_req.createFrequence, name="createFrequenceAPI"),
    path("operaciones_api/frecuencia/modificarFrecuencia", api_fec_req.modifyFrequence, name="modifyFrequenceAPI"),
    path("operaciones_api/frecuencia/eliminarFrecuencia", api_fec_req.deleteFrequence, name="deleteFrequenceAPI"),
    path("operaciones_api/frecuencia/buscarFrecuencia", api_fec_req.searchFrequence, name="searchFrequenceAPI"),
    path("operaciones_api/novedad/mostrarNovedades", api_nov_req.showNovelties, name="showNoveltiesAPI"),
    path("operaciones_api/novedad/crearNovedad", api_nov_req.createNovelty, name="createNoveltyAPI"),
    path("operaciones_api/novedad/modificarNovedad", api_nov_req.modifyNovelty, name="modifyNoveltyAPI"),
    path("operaciones_api/novedad/eliminarNovedad", api_nov_req.deleteNovelty, name="deleteNoveltyAPI"),
    path("operaciones_api/novedad/buscarNovedad", api_nov_req.searchNovelty, name="searchNoveltyAPI"),
    path("operaciones_api/modoFallo/mostrarModos", api_mod_req.showModes, name="showModesAPI"),
    path("operaciones_api/modoFallo/crearModo", api_mod_req.createMode, name="createModeAPI"),
    path("operaciones_api/modoFallo/modificarModo", api_mod_req.modifyMode, name="modifyModeAPI"),
    path("operaciones_api/modoFallo/eliminarModo", api_mod_req.deleteMode, name="deleteModeAPI"),
    path("operaciones_api/modoFallo/buscarModo", api_mod_req.searchMode, name="searchModeAPI"),

    path("operaciones_api/datos_generales_obtenidos", api_acc_v.data_every_month, name="datos_generales_obtenidos"),
    path("operaciones_api/registrar_accidente", api_acc.register_accident, name="registrar_info"),

    # ? MCGREEN - All requests
    # ? General manteinment requests
    path("operaciones_mcgreen/general/mostrarGeneral", mcgreen_g_req.show_general_mant, name="showGeneralMntMCGREEN"),
    path("operaciones_mcgreen/general/crearGeneral", mcgreen_g_req.create_general, name="createGeneralMntMCGREEN"),
    path("operaciones_mcgreen/general/modificarGeneral", mcgreen_g_req.modify_general, name="modifyGeneralMntMCGREEN"),
    path("operaciones_mcgreen/general/eliminarGeneral", mcgreen_g_req.delete_general, name="deleteGeneralMntMCGREEN"),
    # ? Activities requests
    path("operaciones_mcgreen/actividades/crear_actividad", mcgreen_act_req.create_activity, name="createActivityMCGREEN"),
    path("operaciones_mcgreen/actividades/modificarActividad", mcgreen_act_req.modify_activity, name="modifyActivityMCGREEN"),
    path("operaciones_mcgreen/actividades/mostrarActividad", mcgreen_act_req.show_activities, name="showAcivitiesMCGREEN"),
    path("operaciones_mcgreen/actividades/buscarActividad", mcgreen_act_req.search_activity, name="searchActivityMCGREEN"),
    path("operaciones_mcgreen/actividades/eliminarActividad", mcgreen_act_req.delete_activity, name="deleteActivityMCGREEN"),
    path("operaciones_mcgreen/actividades/eliminarActividadCompleto", mcgreen_act_req.delete_activity_with_mant, name="deleteAllActivityMCGREEN"),
    # ? Items requests
    path("operaciones_mcgreen/equipo/mostrarItems", mcgreen_it_req.show_items, name="showItemsMCGREEN"),
    path("operaciones_mcgreen/equipo/modificarItem", mcgreen_it_req.modify_item, name="modifyItemsMCGREEN"),
    path("operaciones_mcgreen/equipo/info_item/<slug:id_item>", item_view, name="itemMCGREEN"),
    path("operaciones_mcgreen/equipo/registrarItem", mcgreen_it_req.create_item, name="createItemMCGREEN"),
    path("operaciones_mcgreen/equipo/buscarItem", mcgreen_it_req.search_item, name="searchItemMCGREEN"),
    path("operaciones_mcgreen/equipo/eliminarItem", mcgreen_it_req.delete_item, name="deleteItemMCGREEN"),
    path("operaciones_mcgreen/equipo/eliminarItemCompleto", mcgreen_it_req.delete_item_complete, name="deleteCompleteItemMCGREEN"),
    path("operaciones_mcgreen/equipo/modificarCaracteristicas", mcgreen_it_req.modify_carateristics, name="modifyCaracteristicsMCGREEN"),
    # ? Manteinment requests
    path("operaciones_mcgreen/correctivo/mostrarCorrectivo", mcgreen_mnt_req.show_corrective_mant, name="showManteinmentsMCGREEN"),
    path("operaciones_mcgreen/correctivo/agregarCorrectivo", mcgreen_mnt_req.create_manteinment, name="createManteinmentMCGREEN"),
    path("operaciones_mcgreen/correctivo/modificarCorrectivo", mcgreen_mnt_req.modify_manteinment, name="modifyManteinmentMCGREEN"),
    path("operaciones_mcgreen/correctivo/eliminarCorrectivo", mcgreen_mnt_req.delete_manteinment, name="deleteManteinmentMCGREEN"),
    # ? Provider requests
    path("operaciones_mcgreen/proveedor/mostrarProveedores", mcgreen_pro_req.show_providers, name="showProvidersMCGREEN"),
    path("operaciones_mcgreen/proveedor/agregarProveedor", mcgreen_pro_req.create_provider, name="createProvidersMCGREEN"),
    path("operaciones_mcgreen/proveedor/agregarProveedorAItem", mcgreen_pro_req.add_provider_to_item, name="addProviderToItemMCGREEN"),
    path("operaciones_mcgreen/proveedor/modificarProveedor", mcgreen_pro_req.modify_provider, name="modifyProvidersMCGREEN"),
    path("operaciones_mcgreen/proveedor/eliminarProveedor", mcgreen_pro_req.delete_provider, name="deleteProvidersMCGREEN"),
    path("operaciones_mcgreen/proveedor/cambiarProveedor", mcgreen_pro_req.change_provider, name="changeProviderToItemMCGREEN"),
    path("operaciones_mcgreen/proveedor/buscarProveedor", mcgreen_pro_req.search_provider, name="searchProviderMCGREEN"),
    path("operaciones_mcgreen/proveedor/quitarProveedor", mcgreen_pro_req.delete_provider_from_item, name="removeProviderToItemMCGREEN"),
    # ? Other requests
    path("operaciones_mcgreen/estado/mostrarEstados", mcgreen_st_req.showStates, name="showStatesMCGREEN"),
    path("operaciones_mcgreen/estado/crearEstado", mcgreen_st_req.createState, name="createStateMCGREEN"),
    path("operaciones_mcgreen/estado/modificarEstado", mcgreen_st_req.modifyState, name="modifyStateMCGREEN"),
    path("operaciones_mcgreen/estado/eliminarEstado", mcgreen_st_req.deleteState, name="deleteStateMCGREEN"),
    path("operaciones_mcgreen/estado/buscarEstado", mcgreen_st_req.searchState, name="searchStateMCGREEN"),
    path("operaciones_mcgreen/frecuencia/mostrarFrecuencias", mcgreen_fec_req.showFrequences, name="showFrequencesMCGREEN"),
    path("operaciones_mcgreen/frecuencia/crearFrecuencia", mcgreen_fec_req.createFrequence, name="createFrequenceMCGREEN"),
    path("operaciones_mcgreen/frecuencia/modificarFrecuencia", mcgreen_fec_req.modifyFrequence, name="modifyFrequenceMCGREEN"),
    path("operaciones_mcgreen/frecuencia/eliminarFrecuencia", mcgreen_fec_req.deleteFrequence, name="deleteFrequenceMCGREEN"),
    path("operaciones_mcgreen/frecuencia/buscarFrecuencia", mcgreen_fec_req.searchFrequence, name="searchFrequenceMCGREEN"),
    path("operaciones_mcgreen/novedad/mostrarNovedades", mcgreen_nov_req.showNovelties, name="showNoveltiesMCGREEN"),
    path("operaciones_mcgreen/novedad/crearNovedad", mcgreen_nov_req.createNovelty, name="createNoveltyMCGREEN"),
    path("operaciones_mcgreen/novedad/modificarNovedad", mcgreen_nov_req.modifyNovelty, name="modifyNoveltyMCGREEN"),
    path("operaciones_mcgreen/novedad/eliminarNovedad", mcgreen_nov_req.deleteNovelty, name="deleteNoveltyMCGREEN"),
    path("operaciones_mcgreen/novedad/buscarNovedad", mcgreen_nov_req.searchNovelty, name="searchNoveltyMCGREEN"),
    path("operaciones_mcgreen/modoFallo/mostrarModos", mcgreen_mod_req.showModes, name="showModesMCGREEN"),
    path("operaciones_mcgreen/modoFallo/crearModo", mcgreen_mod_req.createMode, name="createModeMCGREEN"),
    path("operaciones_mcgreen/modoFallo/modificarModo", mcgreen_mod_req.modifyMode, name="modifyModeMCGREEN"),
    path("operaciones_mcgreen/modoFallo/eliminarModo", mcgreen_mod_req.deleteMode, name="deleteModeMCGREEN"),
    path("operaciones_mcgreen/modoFallo/buscarModo", mcgreen_mod_req.searchMode, name="searchModeMCGREEN"),

    path("operaciones_mcgreen/datos_generales_obtenidos", mcgreen_acc_v.data_every_month, name="datos_generales_obtenidos"),
    path("operaciones_mcgreen/registrar_accidente", mcgreen_acc.register_accident, name="registrar_info"),

    # ? TARCO - All requests
    # ? General manteinment requests
    path("operaciones_tarco/general/mostrarGeneral", tarco_g_req.show_general_mant, name="showGeneralMntTARCO"),
    path("operaciones_tarco/general/crearGeneral", tarco_g_req.create_general, name="createGeneralMntTARCO"),
    path("operaciones_tarco/general/modificarGeneral", tarco_g_req.modify_general, name="modifyGeneralMntTARCO"),
    path("operaciones_tarco/general/eliminarGeneral", tarco_g_req.delete_general, name="deleteGeneralMntTARCO"),
    # ? Activities requests
    path("operaciones_tarco/actividades/crear_actividad", tarco_act_req.create_activity, name="createActivityTARCO"),
    path("operaciones_tarco/actividades/modificarActividad", tarco_act_req.modify_activity, name="modifyActivityTARCO"),
    path("operaciones_tarco/actividades/mostrarActividad", tarco_act_req.show_activities, name="showAcivitiesTARCO"),
    path("operaciones_tarco/actividades/buscarActividad", tarco_act_req.search_activity, name="searchActivityTARCO"),
    path("operaciones_tarco/actividades/eliminarActividad", tarco_act_req.delete_activity, name="deleteActivityTARCO"),
    path("operaciones_tarco/actividades/eliminarActividadCompleto", tarco_act_req.delete_activity_with_mant, name="deleteAllActivityTARCO"),
    # ? Items requests
    path("operaciones_tarco/equipo/mostrarItems", tarco_it_req.show_items, name="showItemsTARCO"),
    path("operaciones_tarco/equipo/modificarItem", tarco_it_req.modify_item, name="modifyItemsTARCO"),
    path("operaciones_tarco/equipo/info_item/<slug:id_item>", item_view, name="itemTARCO"),
    path("operaciones_tarco/equipo/registrarItem", tarco_it_req.create_item, name="createItemTARCO"),
    path("operaciones_tarco/equipo/buscarItem", tarco_it_req.search_item, name="searchItemTARCO"),
    path("operaciones_tarco/equipo/eliminarItem", tarco_it_req.delete_item, name="deleteItemTARCO"),
    path("operaciones_tarco/equipo/eliminarItemCompleto", tarco_it_req.delete_item_complete, name="deleteCompleteItemTARCO"),
    path("operaciones_tarco/equipo/modificarCaracteristicas", tarco_it_req.modify_carateristics, name="modifyCaracteristicsTARCO"),
    # ? Manteinment requests
    path("operaciones_tarco/correctivo/mostrarCorrectivo", tarco_mnt_req.show_corrective_mant, name="showManteinmentsTARCO"),
    path("operaciones_tarco/correctivo/agregarCorrectivo", tarco_mnt_req.create_manteinment, name="createManteinmentTARCO"),
    path("operaciones_tarco/correctivo/modificarCorrectivo", tarco_mnt_req.modify_manteinment, name="modifyManteinmentTARCO"),
    path("operaciones_tarco/correctivo/eliminarCorrectivo", tarco_mnt_req.delete_manteinment, name="deleteManteinmentTARCO"),
    # ? Provider requests
    path("operaciones_tarco/proveedor/mostrarProveedores", tarco_pro_req.show_providers, name="showProvidersTARCO"),
    path("operaciones_tarco/proveedor/agregarProveedor", tarco_pro_req.create_provider, name="createProvidersTARCO"),
    path("operaciones_tarco/proveedor/agregarProveedorAItem", tarco_pro_req.add_provider_to_item, name="addProviderToItemTARCO"),
    path("operaciones_tarco/proveedor/modificarProveedor", tarco_pro_req.modify_provider, name="modifyProvidersTARCO"),
    path("operaciones_tarco/proveedor/eliminarProveedor", tarco_pro_req.delete_provider, name="deleteProvidersTARCO"),
    path("operaciones_tarco/proveedor/cambiarProveedor", tarco_pro_req.change_provider, name="changeProviderToItemTARCO"),
    path("operaciones_tarco/proveedor/buscarProveedor", tarco_pro_req.search_provider, name="searchProviderTARCO"),
    path("operaciones_tarco/proveedor/quitarProveedor", tarco_pro_req.delete_provider_from_item, name="removeProviderToItemTARCO"),
    # ? Other requests
    path("operaciones_tarco/estado/mostrarEstados", tarco_st_req.showStates, name="showStatesTARCO"),
    path("operaciones_tarco/estado/crearEstado", tarco_st_req.createState, name="createStateTARCO"),
    path("operaciones_tarco/estado/modificarEstado", tarco_st_req.modifyState, name="modifyStateTARCO"),
    path("operaciones_tarco/estado/eliminarEstado", tarco_st_req.deleteState, name="deleteStateTARCO"),
    path("operaciones_tarco/estado/buscarEstado", tarco_st_req.searchState, name="searchStateTARCO"),
    path("operaciones_tarco/frecuencia/mostrarFrecuencias", tarco_fec_req.showFrequences, name="showFrequencesTARCO"),
    path("operaciones_tarco/frecuencia/crearFrecuencia", tarco_fec_req.createFrequence, name="createFrequenceTARCO"),
    path("operaciones_tarco/frecuencia/modificarFrecuencia", tarco_fec_req.modifyFrequence, name="modifyFrequenceTARCO"),
    path("operaciones_tarco/frecuencia/eliminarFrecuencia", tarco_fec_req.deleteFrequence, name="deleteFrequenceTARCO"),
    path("operaciones_tarco/frecuencia/buscarFrecuencia", tarco_fec_req.searchFrequence, name="searchFrequenceTARCO"),
    path("operaciones_tarco/novedad/mostrarNovedades", tarco_nov_req.showNovelties, name="showNoveltiesTARCO"),
    path("operaciones_tarco/novedad/crearNovedad", tarco_nov_req.createNovelty, name="createNoveltyTARCO"),
    path("operaciones_tarco/novedad/modificarNovedad", tarco_nov_req.modifyNovelty, name="modifyNoveltyTARCO"),
    path("operaciones_tarco/novedad/eliminarNovedad", tarco_nov_req.deleteNovelty, name="deleteNoveltyTARCO"),
    path("operaciones_tarco/novedad/buscarNovedad", tarco_nov_req.searchNovelty, name="searchNoveltyTARCO"),
    path("operaciones_tarco/modoFallo/mostrarModos", tarco_mod_req.showModes, name="showModesTARCO"),
    path("operaciones_tarco/modoFallo/crearModo", tarco_mod_req.createMode, name="createModeTARCO"),
    path("operaciones_tarco/modoFallo/modificarModo", tarco_mod_req.modifyMode, name="modifyModeTARCO"),
    path("operaciones_tarco/modoFallo/eliminarModo", tarco_mod_req.deleteMode, name="deleteModeTARCO"),
    path("operaciones_tarco/modoFallo/buscarModo", tarco_mod_req.searchMode, name="searchModeTARCO"),

    path("operaciones_tarco/datos_generales_obtenidos", tarco_acc_v.data_every_month, name="datos_generales_obtenidos"),
    path("operaciones_tarco/registrar_accidente", tarco_acc.register_accident, name="registrar_info"),
]