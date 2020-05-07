'''
This script tests the registration and login process.
TODO:
    - Delete user
    - Update personal data
    - Read personal data
'''
from django.test import TestCase, Client
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.models import User
from specialpark.tests import success, decode_response

class TestUsers(TestCase):
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

    def test_register_user(self):
        self.body = {
            'email': 'graven@gmail.com',
            'password1': 'test123OK',
            'password2': 'test123OK'
        }

        self.request = self.client.post(self.url, self.body)

        try:
            user = User.objects.get(email='graven@gmail.com')
            success('User registration')
        except ObjectDoesNotExist:
            assert False
    
    def test_login_user(self):
        self.url = '/users/login/'
        self.body = {
            'username': 'joker1234',
            'email': 'joker1234@example.com',
            'password': 'vitamineD'
        }
        
        self.request = self.client.post(self.url, self.body)
        self.response = decode_response(self.request.content)

        try:
            self.key = self.response['key']
            success('User authentication')
        except KeyError:
            assert False
    
    def test_delete_user(self):
        # ! Deleting a user with Authorization Token
        # ? Coming soon
        success('Delete user')
