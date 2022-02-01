from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Bin, Location


class LocationEncoder(ModelEncoder):
    model = Location
    properties = [
        "id",
        "closet_name",
        "section_number",
        "shelf_number",
    ]


class BinEncoder(ModelEncoder):
    model = Bin
    properties = [
        "id",
        "closet_name",
        "bin_number",
        "bin_size",
    ]


@require_http_methods(["GET", "POST"])
def api_locations(request):
    """
    Collection RESTful API handler for Location objects in
    the wardrobe.

    GET:
    Returns a dictionary with a single key "locations" which
    is a list of the closet name, section number, and shelf
    number for the location, along with its href and id.

    {
        "locations": [
            {
                "id": database id for the location,
                "closet_name": location's closet name,
                "section_number": the number of the wardrobe section,
                "shelf_number": the number of the shelf,
                "href": URL to the location,
            },
            ...
        ]
    }

    POST:
    Creates a location resource and returns its details.
    {
        "closet_name": location's closet name,
        "section_number": the number of the wardrobe section,
        "shelf_number": the number of the shelf,
    }
    """
    if request.method == "GET":
        locations = Location.objects.all()
        return JsonResponse(
            {"locations": locations},
            encoder=LocationEncoder,
        )
    else:
        content = json.loads(request.body)
        location = Location.objects.create(**content)
        return JsonResponse(
            location,
            encoder=LocationEncoder,
            safe=False,
        )

@require_http_methods(["DELETE", "GET", "PUT"])
def api_location(request, pk):
    """
    Single-object API for the Location resource.

    GET:
    Returns the information for a Location resource based
    on the value of pk
    {
        "id": database id for the location,
        "closet_name": location's closet name,
        "section_number": the number of the wardrobe section,
        "shelf_number": the number of the shelf,
        "href": URL to the location,
    }

    PUT:
    Updates the information for a Location resource based
    on the value of the pk
    {
        "closet_name": location's closet name,
        "section_number": the number of the wardrobe section,
        "shelf_number": the number of the shelf,
    }

    DELETE:
    Removes the location resource from the application
    """
    if request.method == "GET":
        try:
            location = Location.objects.get(id=pk)
            return JsonResponse(
                location,
                encoder=LocationEncoder,
                safe=False
            )
        except Location.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            location = Location.objects.get(id=pk)
            location.delete()
            return JsonResponse(
                location,
                encoder=LocationEncoder,
                safe=False,
            )
        except Location.DoesNotExist:
            return JsonResponse({"message": "Does not exist"})
    else: # PUT
        try:
            content = json.loads(request.body)
            location = Location.objects.get(id=pk)

            props = ["closet_name", "shelf_number", "section_number"]
            for prop in props:
                if prop in content:
                    setattr(location, prop, content[prop])
            location.save()
            return JsonResponse(
                location,
                encoder=LocationEncoder,
                safe=False,
            )
        except Location.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response


@require_http_methods(["GET", "POST"])
def api_bins(request):
    """
    Collection RESTful API handler for Bin objects in
    the wardrobe.

    GET:
    Returns a dictionary with a single key "bins" which
    is a list of the closet name, bin number, and bin size
    for the bin, along with its href and id.

    {
        "bins": [
            {
                "id": database id for the bin,
                "closet_name": bin's closet name,
                "bin_number": the number of the bin,
                "bin_size": the size of the bin,
                "href": URL to the bin,
            },
            ...
        ]
    }

    POST:
    Creates a bin resource and returns its details.
    {
        "closet_name": bin's closet name,
        "bin_number": the number of the bin,
        "bin_size": the size of the bin,
    }
    """
    if request.method == "GET":
        bin = Bin.objects.all()
        return JsonResponse(
            {"bins": bin},
            encoder=BinEncoder,
        )
    else:
        content = json.loads(request.body)
        bin = Bin.objects.create(**content)
        return JsonResponse(
            bin,
            encoder=BinEncoder,
            safe=False,
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def api_bin(request, pk):
    """
    Single-object API for the Bin resource.

    GET:
    Returns the information for a Bin resource based
    on the value of pk
    {
        "id": database id for the bin,
        "closet_name": bin's closet name,
        "bin_number": the number of the bin,
        "bin_size": the size of the bin,
        "href": URL to the bin,
    }

    PUT:
    Updates the information for a Bin resource based
    on the value of the pk
    {
        "closet_name": bin's closet name,
        "bin_number": the number of the bin,
        "bin_size": the size of the bin,
    }

    DELETE:
    Removes the bin resource from the application
    """
    if request.method == "GET":
        try:
            bin = Bin.objects.get(id=pk)
            return JsonResponse(
                bin,
                encoder=BinEncoder,
                safe=False
            )
        except Bin.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            bin = Bin.objects.get(id=pk)
            bin.delete()
            return JsonResponse(
                bin,
                encoder=BinEncoder,
                safe=False,
            )
        except Bin.DoesNotExist:
            return JsonResponse({"message": "Does not exist"})
    else: # PUT
        try:
            content = json.loads(request.body)
            bin = Bin.objects.get(id=pk)

            props = ["closet_name", "bin_number", "bin_size"]
            for prop in props:
                if prop in content:
                    setattr(bin, prop, content[prop])
            bin.save()
            return JsonResponse(
                bin,
                encoder=BinEncoder,
                safe=False,
            )
        except Bin.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
