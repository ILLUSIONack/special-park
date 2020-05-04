from ast import literal_eval
from django.test import TestCase, Client
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.models import User
from tests import success

class TestViews(TestCase):
    client = Client()
    user = {
        'username': 'joker1234',
        'email': 'joker1234@example.com',
        'password1': 'vitamineD',
        'password2': 'vitamineD'
    }

    def setUp(self):
        # Request details
        url = '/users/registration/'
        body = {
            'username': self.user['username'],
            'email': self.user['email'],
            'password1': self.user['password1'],
            'password2': self.user['password2']
        }
        
        # Making the request
        request = self.client.post(url, body)

    def test_register_user(self):
        # Request details
        url = '/users/registration/'
        body = {
            'username': 'johan_vander_graven',
            'email': 'graven@gmail.com',
            'password1': 'test123OK',
            'password2': 'test123OK'
        }
        
        # Making the request
        request = self.client.post(url, body)

        # Verifying if user exists
        user = User.objects.get(username=self.user['username'])
        success('test_register_user')
    
    def test_login_user(self):
        # Request details
        url = '/users/login/'
        body = {
            'username': self.user['username'],
            'email': self.user['email'],
            'password': self.user['password1']
        }
        
        # Making the request
        request = self.client.post(url, body)

        # Converting str to dict
        response = literal_eval(request.content.decode('utf-8'))

        try:
            key = response['key']
            success('test_login_user')
        except KeyError:
            assert False
