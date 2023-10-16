import json
from .models import Shoe
from django.http import JsonResponse
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods
# from django.shortcuts import render

class ShoeListEncoder(ModelEncoder):
  model = Shoe
  properties = ["name"]

# API_LIST_SHOES
@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
  if request.method == "GET":
    shoes = Shoe.objects.all()

    return JsonResponse(
      { "shoes": shoes },
      encoder=ShoeListEncoder,
      safe=False
    )
  else:
    content = json.loads(request.body)

    shoe = Shoe.objects.create(**content)
    return JsonResponse(
      shoe,
      encoder=ShoeListEncoder,
      safe=False,
    )
