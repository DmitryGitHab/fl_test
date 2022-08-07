import requests


HOST = 'http://127.0.0.1:5000'

# response = requests.get(HOST)
# print(response.status_code)
# print(response.text)

response = requests.post(f'{HOST}/test/', json={'key': 'value'}, headers={'token': 'dfge494g3'}, params={'k1': 'v1'})
print(response.status_code)
print(response.text)