from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Hats


# Create your views here.

# class LocationVOEncoder(ModelEncoder):
#     model = LocationVO
#     properties = [
#         "name",
#         "import_href",
#         ]


# class HatsListEncoder(ModelEncoder):
#     model = Hats
#     properties = ["name"]


# class HatsDetailEncoder(ModelEncoder):
#     model = Hats
#     properties = [
#         "name",
#         "fabric",
#         "style",
#         "color",
#         "picture_url",
#         ]
#     encoders = {
#         "location": LocationVOEncoder(),
#     }


@require_http_methods(["GET", "POST"])
def api_hats_list(request):
        # if location_vo_id:
        #     hats = Hats.objects.filter(location=location_vo_id)
        # else:
        if request.method == "GET":
            hats = Hats.objects.all()
        return JsonResponse(
            {"hats": hats},
          
        )
    # else:
    #     content = json.loads(request.body)

    #     try:
    #         location_href = f"/api/locations/{location_vo_id}"
    #         location = LocationVO.objects.get(import_href=location_href)
    #         content["location"] = location
    #     except LocationVO.DoesNotExist:
    #         return JsonResponse(
    #             {"error": "Location does not exist"},
    #             status=404,
    #         )
    #     hats = Hats.objects.create(**content)
    #     return JsonResponse(
    #         hats,
    #         encoder=HatsDetailEncoder,
    #         safe=False,
    #     )



