from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Car, CustomerUser
from .serializers import CarSerializer, CustomerSerializer
from .services import RequestHandler, CarService, CustomerService, SerializerHandler
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def user_car(request):
    # Initializing the needed classes for the endpoint
    serializer_handler = SerializerHandler()
    request_handel = RequestHandler(request)
    request_handel.add_user_id_to_dictionary('owner')

    # Handling the request methods
    if request.method == "POST":
        request_handel.capitalize_license_plate()
        serializer_handler.createInstance(
            serializer=CarSerializer(data=request_handel.get_dictionary()),
            newObjectsMessage='new_car', message='new car has been added!')
        return JsonResponse(serializer_handler.data, status=serializer_handler.status)

    elif request.method == "GET":
        cars = Car.objects.filter(owner_id=request_handel.get_user_id())
        cars_response = {}
        for car in cars:
            serializer = CarSerializer(car)
            cars_response[serializer.data['license_plate_number']] = serializer.data
        return JsonResponse({'cars': cars_response}, status=201)

@api_view(["DELETE", "PUT"])
@permission_classes([IsAuthenticated])
def edit_car(request):
    # Initializing the needed classes for the endpoint
    request_handel = RequestHandler(request)
    request_handel.add_user_id_to_dictionary("owner")
    request_handel.capitalize_license_plate()
    serializer_handler = SerializerHandler()
    try:
        car = Car.objects.get(license_plate_number=request_handel.get_value_from_request_dict('license_plate_number'))
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Auto bestaat niet'})

    # Handling the request methods
    if request.method == 'DELETE':
        car.delete()
        return JsonResponse({'message': 'car deleted'})

    elif request.method == 'PUT':
        request_handel.swap_element_in_dictionary('new_license_plate_number','license_plate_number')
        serializer_handler.updateInstance(
            CarSerializer(car,
                          data=request_handel.get_dictionary()),
            newObjectsMessage='updated car', message='Jouw voertuig is aangepast!')
        return JsonResponse(serializer_handler.data, status=serializer_handler.status)

@api_view(["GET", "POST", "PUT"])
@permission_classes([IsAuthenticated])
def user_info(request):
    # Initializing the needed classes for the endpoint
    serializer_handler = SerializerHandler()
    request_handel = RequestHandler(request)
    request_handel.add_user_id_to_dictionary('user')

    # Handling the request methods
    if request.method == 'GET':
        customer_service = CustomerService(request.user.id)
        customer = customer_service.getCustomer()
        serializer_handler.setObjectSerializer(CustomerSerializer(customer))
        data = serializer_handler.getInstance()
        return JsonResponse(data)

    elif request.method == 'POST':
        serializer_handler.createInstance(
            serializer=CustomerSerializer(data=request_handel.get_dictionary()),
            newObjectsMessage='newCustomer', message='Customer created')
        return JsonResponse(serializer_handler.data, status=serializer_handler.status)

    elif request.method == 'PUT':
        customer_service = CustomerService(request.user.id)
        customer = customer_service.getCustomer()
        serializer_handler.updateInstance(
            CustomerSerializer(customer, data=request_handel.get_dictionary()), 'updated_customer',
            'customer updated!')
        return JsonResponse(serializer_handler.data, status=serializer_handler.status)