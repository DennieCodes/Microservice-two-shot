from .models import Shoe
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
# from django.shortcuts import render

# API_LIST_SHOES
@require_http_methods(["GET"])
def api_list_shoes(request):
  # shoes = Shoe.objects.all()

  shoes = { "name": "Nike"}

  return JsonResponse(
    { "shoes": shoes },
  )
