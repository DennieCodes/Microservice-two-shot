from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Hats
from common.json import ModelEncoder


# class LocationVODetailEncoder(ModelEncoder):
#     model = LocationVO
#     properties = [
#         "closet_name",
#         "import_href",
#         "section_number",
#         "shelf_number",
#         ]


class HatsListEncoder(ModelEncoder):
    model = Hats
    properties = [
        "style"#!<<styleName
        # "id",
        # "location",
        # "color",
        # "picture_url",
        # "fabric",

        ]

    #get extra data here
    # def get_extra_data(self, o):
    #     return {"location": o.location.closet_name}

# class HatsDetailEncoder(ModelEncoder):
#     model = Hats
#     properties = [
#         "id",
#         "name",
#         "fabric",
#         "style",#!<<not name...
#         "color",
#         "picture_url",
#         "location",#!<<<put this back in...
#         ]
#     encoders = {
#         "location": LocationVODetailEncoder(),
#     }

    # def get_extra_data(self, o):
    #     return {"location": o.location.id}


@require_http_methods(["GET", "POST"])
def api_hats_list(request): #location_vo_id=None):
    if request.method == "GET":
        # if location_vo_id is not None:
        #     hats = Hats.objects.filter(location=location_vo_id)
        # else:
        hats = Hats.objects.all()
       
        #     #?hats_list = HatsListEncoder().encode(hats_list)
        return JsonResponse(
            {"hats": hats},
            encoder=HatsListEncoder,
        )
    else:
        content = json.loads(request.body)
        print(content)

        # try:
#             location = LocationVO.objects.get(import_href=content["location"])

#             content["location"] = location
#             print("location: ",location)#!<<keep here for now...
            # except 
            # return JsonResponse(
            #     {"error": "Location does not exist"},
            #     status=400,
            # )
        hats = Hats.objects.create(**content)
        return JsonResponse(
            hats,
            encoder=HatsListEncoder,
            safe=False,
        )

# @require_http_methods(["GET", "DELETE", "PUT"])
# def api_hats_detail(request, pk):
#     if request.method == "GET":
#         hats = Hats.objects.get(id=pk)
#         return JsonResponse(
#             hats,
#             encoder=HatsDetailEncoder,
#             safe=False,
#         )
#     elif request.method == "DELETE":
#         count, _ = Hats.objects.filter(id=pk).delete()
#         return JsonResponse(
#             {"Deleted": count > 0},
#         )

#     else:
#         content = json.loads(request.body)
#         try:
#             if "location" in content:
#                 location = LocationVO.objects.get(import_href=content["location"])
#                 content["location"] = location
#         except LocationVO.DoesNotExist:
#             return JsonResponse(
#                 {"error": "Location does not exist"},
#                 status=400,
#             )
#         Hats.objects.filter(id=pk).update(**content)
#         hats = Hats.objects.get(id=pk)
#         return JsonResponse(
#             hats,
#             encoder=HatsDetailEncoder,
#             safe=False,
#         )


# @require_http_methods(["GET"])
# def api_list_locations(request):
#     locations = LocationVO.objects.all()
#     return JsonResponse(
#         {"locations": locations},
#         encoder=LocationVODetailEncoder,
#     )
