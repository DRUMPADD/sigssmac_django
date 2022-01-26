from django.urls import path

from sigss_principal.views import principal


urlpatterns = [
    path("", principal, name="inicio")
]