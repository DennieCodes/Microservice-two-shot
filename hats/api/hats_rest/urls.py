from django.urls import path
from .views import api_hats_list
urlpatterns = [
    # path('hats/<int:pk>/', api_hats_detail, name='api_hats_detail'),

    # path('locations/', api_list_locations, name='api_list_locations'),
    # path('locations/<int:location_vo_id>/hats/', api_hats_list, name='api_hats_list'),
    path('hats/', api_hats_list, name='api_create_hats'),
]

