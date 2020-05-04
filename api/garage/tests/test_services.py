# from ast import literal_eval
# from django.test import TestCase, Client
# from django.contrib.auth.models import User

# class TestVisitor(TestCase):
#     client = Client()
#     user = {
#         'username': 'joker1234',
#         'email': 'joker1234@example.com',
#         'password1': 'vitamineD',
#         'password2': 'vitamineD'
#     }

#     def setUp(self):
#         # Request details
#         url = '/users/registration/'
#         body = {
#             'username': self.user['username'],
#             'email': self.user['email'],
#             'password1': self.user['password1'],
#             'password2': self.user['password2']
#         }

#         # Making the request
#         request = self.client.post(url, body)
#         request = literal_eval(request.content.decode('utf-8'))

#         # Obtaining the token
#         self.token = request['key']

#         # Add a license
#         url = '/users/car/'
#         body = {
#             "license_plate_number":"46-nn-sr",
#             "license_country_code": "NL"
#         }
#         header = {
#             'Authorization': f'Token {self.token}'
#         }

#         print('running')
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
#         adding = self.client.post(url, body)
        
#     # Test an empty license request.
#     def test_empty_license_request(self):
#         print(self.token)

#     # Test an invalid license
#     def test_invalid_license(self):
#         pass

#     # Test an license which is not a customer
#     def test_license_no_customer(self):
#         pass

#     # Test a existing client who wants to enter
#     def test_existing_client_entering(self):
#         pass
    
#     # Test a existing client who wants to leave
#     def test_existing_client_leaving(self):
#         pass
