'''
This script tests the parking logic of the application. A car can drive in and out of a parking garage, this script tests if the data gets added to the correct tables and how the customer requests is handled. Also different requests are tested for example: requests which are empty or invalid, requests with licenses plates which are not clients.
'''
from django.test import TestCase, Client
from users.tests.test_license_plates import TestLicensePlates
from garage.models import Garage, TimeTable
from users.models import Car, Transactions
from django.contrib.auth.models import User
from django.db.models.base import ObjectDoesNotExist
from specialpark.tests import success

class TestParkingLogic(TestCase):
    def setUp(self):
        self.license_plate = '46-NN-SR'
        TestLicensePlates.setUp(self)
        TestLicensePlates.test_add_license(self, False, self.license_plate)
        self.car = Car.objects.get(license_plate_number=self.license_plate)
        self.garage = Garage(name='Q Park', address='Wijnhaven', address_number='107', country_code='NL', hourly_rate=2, opening_time='00:00', closing_time='00:00', currency='EUR', owner=User.objects.get(email='joker1234@example.com'))
        self.garage.save()

    def test_empty_request(self):
        self.url = f'/garage/port/'
        self.request = self.client.post(self.url)
        self.url = f'/garage/port/?license='
        self.request = self.client.post(self.url)

        if len(TimeTable.objects.all()) == 0 and len(Transactions.objects.all()) == 0:
            success('Empty requests')
        else:
            assert False

    def test_invalid_request(self):
        self.url = f'/garage/port/?license=nskfjn'
        self.request = self.client.post(self.url)

        if len(TimeTable.objects.all()) == 0 and len(Transactions.objects.all()) == 0:
            success('Invalid requests')
        else:
            assert False
    
    def test_request_from_non_client(self):
        self.url = f'/garage/port/?license=32-GG-MU'
        self.request = self.client.post(self.url)

        if len(TimeTable.objects.all()) == 0 and len(Transactions.objects.all()) == 0:
            success('Not a client requests')
        else:
            assert False
    
    def test_request_from_existing_client_entering(self, msg=True):
        self.url = f'/garage/port/?license={self.license_plate}'
        self.request = self.client.post(self.url)

        try:
            self.time = TimeTable.objects.get(car=self.car)
            success('Existing client request (entering)') if msg else None
        except ObjectDoesNotExist as err:
            print(f'error: {err}')
            assert False

    def test_request_from_existing_client_leaving(self):
        self.test_request_from_existing_client_entering(False)
        self.url = f'/garage/port/?license={self.license_plate}'
        self.request = self.client.post(self.url)
        self.trans = Transactions.objects.get(car=self.car)

        if self.trans and len(TimeTable.objects.all()) == 0:
            success('Existing client request (leaving)')
        else:
            assert False
