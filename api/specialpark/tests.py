from ast import literal_eval
from simple_chalk import green

def success(test_name):
    print(' '*3, green.bold('passed'), green.bold(u'\u2713'), f'- {test_name}')

def decode_response(res):
    return literal_eval(res.decode('utf-8'))
