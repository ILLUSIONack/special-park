from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Car, Garage
from .serializers import TimeTableSerializer, GarageSerializer
from users.services import RequestHandler, CarService, CustomerService
from rest_framework import status
from . services import TimeTableService
from django.contrib.auth.models import User

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


@api_view(["DELETE", "PUT", "POST"])
@permission_classes([IsAuthenticated])
def time_table(request):
    if request.method == "POST":
        serializer = TimeTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'newCar': serializer.data, 'message': 'Car has entered the garage'}, status=201)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "PUT":
        request_handel = RequestHandler(request)
        time_table = TimeTableService(license_plate=request.data['car'], garage_id=request.data['garage'])
        request_handel.add_to_dictionary('check_in_time', time_table.getCheckInTime())
        serializer = TimeTableSerializer(time_table.getTimeTable(), data=request_handel.get_dictionary())
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Car has left'})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

