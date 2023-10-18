import json
from .models import Shoe, BinVO
from django.http import JsonResponse
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods
# from django.shortcuts import render

class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = ["closet_name", "import_href"]

class ShoeListEncoder(ModelEncoder):
  model = Shoe
  properties = ["model_name", "manufacturer_name", "color", "picture_url", "assigned_bin", "id"]
  encoders = {"assigned_bin": BinVOEncoder()}

# API_LIST_SHOES
@require_http_methods(["GET", "POST"])
def api_list_shoes(request, bin_vo_id=None):
  if request.method == "GET":
    if bin_vo_id is not None:
      shoe = Shoe.objects.filter(assigned_bin=bin_vo_id)
    else:
      shoes = Shoe.objects.all()

    return JsonResponse(
      { "shoes": shoes },
      encoder=ShoeListEncoder,
      safe=False
    )
  else:
    content = json.loads(request.body)

    # print("Content: ", content)
    test_bin = BinVO.objects.all().values()
    print("Bin: ", len(test_bin))

    try:
      bin_href = content["assigned_bin"]
      assigned_bin = BinVO.objects.get(import_href=bin_href)


      content['assigned_bin'] = assigned_bin
    except BinVO.DoesNotExist:
      return JsonResponse(
          {"message": "Invalid bin id"},
          status=400,
      )

    shoe = Shoe.objects.create(**content)
    return JsonResponse(
      shoe,
      encoder=ShoeListEncoder,
      safe=False,
    )

# API_SHOW_SHOE
@require_http_methods(["GET", "DELETE"])
def api_show_shoe(request, pk):
  if request.method == "GET":
    shoe = Shoe.objects.get(id=pk)
    return JsonResponse(
      {"shoe": shoe},
      encoder=ShoeListEncoder,
      safe=False,
    )
  else:
    count, _ = Shoe.objects.filter(id=pk).delete()
    return JsonResponse({"deleted": count > 0})
