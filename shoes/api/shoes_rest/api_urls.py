from django.urls import path
from .api_views import api_list_shoes

urlpatterns = [
  path("shoes/", api_list_shoes, name="api_list_shoes"),
]