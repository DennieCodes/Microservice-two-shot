from .models import Shoe
from django.http import JsonResponse
# from django.shortcuts import render

def api_list_shoes(request):
  shoes = Shoe.objects.all()

  return JsonResponse(
    { "shoes": shoes},
  )
