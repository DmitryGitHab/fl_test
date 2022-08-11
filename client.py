import requests
# from flask import request

HOST = 'http://127.0.0.1:5000'
# response = requests.post(f'{HOST}/test/', json={'key': 'value'}, headers={'token': 'dfge494g3'}, params={'k1': 'v1'})

# response = requests.post(f'{HOST}/users/', json={'name': 'user_0', 'password': '1234'})
# print(response.status_code)
# print(response.text)
#
response = requests.patch(f'{HOST}/users/1', json={'name': 'user_1_v2'})
print(response.status_code)
print(response.text)


response = requests.get(f'{HOST}/users/2')
print(response.status_code)
print(response.text)

response = requests.delete(f'{HOST}/users/3')
print(response.status_code)
print(response.text)
