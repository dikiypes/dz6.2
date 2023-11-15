from django.urls import path
from catalog.views import index_catalog, contact
# from . import views
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("", index_catalog),
    path("contact/", contact),
]
