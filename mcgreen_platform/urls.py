from django.urls import path
from mcgreen_platform.views import *

urlpatterns = [
    path("", index, name="generalMantMCGREEN"),
    path("actividades", activities, name="activitiesMCGREEN  "),
    path("equipos", items, name="itemsMCGREEN"),
    path("mantenimiento-correctivo", correc_manteinment, name="corMantMCGREEN"),
    path("otros-registros", other_views, name="otherRegistersMCGREEN"),
]