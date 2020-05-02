from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Garage
from .serializers import GarageSerializer
from users.services import RequestHandler, CustomerService
from rest_framework import status
from .services import Visitor

# TODO:
# Handle objects that does not exists with correct error handling
# Code clean up( use the serializerhandler class)

@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def garage(request):
    customer = CustomerService(request.user.id)
    request_handel = RequestHandler(request)
    request_handel.add_user_id_to_dictionary('owner')

    if customer.is_garage_owner():
        if request.method == "POST":
            serializer = GarageSerializer(data=request_handel.get_dictionary())
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'new_garage': serializer.data, 'message': 'Garage added!'}, status=201)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'GET':
            garages = Garage.objects.filter(owner_id=request_handel.get_user_id())
            garage_response = {}
            for garage in garages:
                serializer = GarageSerializer(garage)
                garage_response[serializer.data['id']] = serializer.data
                continue
            return JsonResponse({'garages': garage_response}, status=201)
    else:
        return JsonResponse({'Message': 'Unauthorized access'})

@api_view(["POST"])
@permission_classes([])
def time_table(request, **kwargs):
    license = request.GET.get('license')
    visitor = Visitor(license)
    return visitor.response()