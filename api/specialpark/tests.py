from ast import literal_eval
from simple_chalk import green

def success(test_name):
    print(f'{test_name} -', green.bold('passed'), u'\u2713')

def decode_response(res):
    return literal_eval(res.decode('utf-8'))
