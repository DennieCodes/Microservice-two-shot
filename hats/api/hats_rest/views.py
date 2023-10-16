from django.shortcuts import render
from .models import Hats


def api_hats_list(request, location_vo_id=None):
    if request.method == "GET":
        if location_vo_id is not None:
            hats = Hats.objects.filter(location=location_vo_id)
        else:
            hats = Hats.objects.all()

        return JsonResponse(
            {"hats": hats
        )


