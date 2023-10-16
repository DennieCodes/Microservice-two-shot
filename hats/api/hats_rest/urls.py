from django.urls import path
from .views import api_hats_list

urlpatterns = [
    path('hats/', api_hats_list, name='api_hats_list'),
]
