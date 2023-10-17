from django.urls import path
from .api_views import api_list_hats, api_delete_hat


urlpatterns = [
    # SHOW all hats
    path('hats/', api_list_hats, name='api_list_hats'),

    # GET hats from a specific location
    path('locations/<int:location_vo_id>/hats/', api_list_hats, name='api_detail_hats'),

    # DELETE a specific hat
    path('hats/<int:id>/', api_delete_hat, name='api_delete_hat')
]
