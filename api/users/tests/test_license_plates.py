'''
This script tests the CRUD operations for the license plates. A user create, read, update and delete a license plate.
'''
from django.test import TestCase, Client
from users.models import Car
from django.db.models.base import ObjectDoesNotExist
from specialpark.tests import success, decode_response

class TestLicensePlates(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/users/registration/'
        self.body = {
            'username': 'joker1234',
            'email': 'joker1234@example.com',
            'password1': 'vitamineD',
            'password2': 'vitamineD'
        }
        
        self.request = self.client.post(self.url, self.body)
        self.response = decode_response(self.request.content)
        self.token = { 'Authorization': 'Token ' + self.response['key'] }

    def test_add_license(self, msg=True, license_plate='46-NN-SR'):
        self.url = '/users/car/'
        self.body = {
            'license_plate_number': license_plate,
            'license_country_code': 'NL'
        }

        self.request = self.client.post(self.url, content_type='application/json', data=self.body, **self.token)
        self.msg = decode_response(self.request.content)

        try:
            car = Car.objects.get(license_plate_number=license_plate)
            success('Add license plate') if msg else None
        except ObjectDoesNotExist:
            assert False

    def test_list_all_licenses(self, msg=True):
        self.test_add_license(False, '46-NN-SR')
        self.test_add_license(False, '77-JE-MO')
        self.url = '/users/car/'

        self.request = self.client.get(self.url, **self.token)
        self.msg = decode_response(self.request.content)

        if self.msg['cars']:
            success('List all licenses') if msg else None
            return self.msg['cars']
        assert False

    def test_edit_license(self):
        self.test_add_license(False, '23-EK-DD')
        self.url = '/users/edit_car/'
        self.body = {
	        'license_plate_number':'23-EK-DD',
	        'new_license_plate_number':'23-EK-TT',
	        'license_country_code': 'NL'
        }

        self.request = self.client.put(self.url, content_type='application/json', data=self.body, **self.token)
        self.response = decode_response(self.request.content)

        self.cars = self.test_list_all_licenses(False)

        if self.cars['23-EK-TT'] and self.cars.get('23-EK-DD') == None and self.response['message']:
            return success('Edit a license')
        assert False

    # ! Delete coming soon
    # def test_delete_license(self):
    #     self.test_add_license(False, '55-EK-UU')
    #     self.test_add_license(False, '66-TY-UU')

    #     self.url = '/users/edit_car/55-EK-UU'
    #     self.request = self.client.delete(self.url, **self.token)
        
    #     self.cars = self.test_list_all_licenses(False)

    #     success('Delete a license')
