import json
from .models import Car, CustomerUser
from .serializers import CarSerializer, CustomerSerializer
from django.http import JsonResponse

class SerializerHandler:
    objectSerializer = None
    objectModel = None
    status = None
    data = None

    def setObjectSerializer(self, objectSerializer):
        self.objectSerializer = objectSerializer

    def setObjectModel(self, objectModel):
        self.objectModel = objectModel

    # Takes in serializer with data and checks wether the data is valid in order to create a new instance
    def createInstance(self, serializer, newObjectsMessage, message):
        if serializer.is_valid():
            serializer.save()
            self.data = {newObjectsMessage: serializer.data, 'message': message}
            self.status = 201
            return
        self.data = serializer.errors
        self.status = 400

    # Takes in serializer with data and checks wether the data is valid in order to update a existing instance
    def updateInstance(self, serializer, newObjectsMessage, message):
        if serializer.is_valid():
            serializer.save()
            self.data = {newObjectsMessage: serializer.data, 'message': message}
            self.status = 201
            return
        self.data = serializer.errors
        self.status = 400

    def getInstance(self):
        return self.objectSerializer.data

class RequestHandler:
    dictionary = None
    request_object = None

    def __init__(self, request_object):
        self.dictionary = request_object.data
        self.request_object = request_object

    def add_user_id_to_dictionary(self, key_name):
        self.dictionary[key_name] = self.request_object.user.id

    def add_to_dictionary(self, key_name, value):
        self.dictionary[key_name] = value

    def get_dictionary(self):
        return self.dictionary

    def get_user_id(self):
        return self.request_object.user.id

    def get_value_from_request_dict(self, key):
        return self.dictionary[str(key)]

    def add_car_id_to_dict(self, key_name, car_object):
        self.dictionary[key_name] = self.car_object.id

class CarService:
    car = None

    def __init__(self, license_plate):
        self.car = Car.objects.get(license_plate_number=license_plate)

    def getCar(self):
        return self.car

    def deleteCar(self):
        self.car.delete()
        print("car deleted")

class CustomerService:
    customer = None

    def __init__(self, request_user_id):
        self.customer = CustomerUser.objects.get(user_id=request_user_id)

    def getCustomer(self):
        return self.customer

    def deleteCar(self):
        self.customer.delete()

    def is_garage_owner(self):
        return self.customer.is_garage_owner