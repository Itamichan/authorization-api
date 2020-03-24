import requests
import json

response = requests.post('http://localhost:5000/api/v1/registration', data=json.dumps({
    'username': 'cristina23',
    'password': 'helooo23,',
    'email': 'ana25@gmail.com'
}), headers={'Content-Type': 'application/json'})

print(response.status_code, response.json())
assert response.status_code == 200, 'Endpoint does not respond with 200'

response = requests.post('http://localhost:5000/api/v1/login', data=json.dumps({
    'username': 'cristina23',
    'password': 'helooo23,'
}), headers={'Content-Type': 'application/json'}, timeout=1)

print(response.status_code, response.content)
assert response.status_code == 200, 'Endpoint does not respond with 200'
assert 'token' in response.json(), 'Response dict has no token inside'

jwt = response.json()['token']
print("Token", jwt)

response = requests.get('http://localhost:5000/api/v1/profile', headers={
    'Authorization': f'JWT {jwt}'
})

print(response.status_code, response.json())
assert response.status_code == 200, 'Secret Endpoint does not respond with 200'

response = requests.get('http://localhost:5000/api/v1/profile', headers={
    'Authorization': f'JWT bad token'
})

print(response.status_code, response.json())
assert response.status_code == 403, 'Secret Endpoint does not respond with 403 on abd token'

response = requests.patch('http://localhost:5000/api/v1/profile', data=json.dumps({
    'new_secret': 'I also like cats.'
}), headers={'Content-Type': 'application/json',
             'Authorization': f'JWT {jwt}'})

print(response.status_code, response.json())
assert response.status_code == 200, 'Endpoint does not respond with 200'

response = requests.delete('http://localhost:5000/api/v1/profile',
                           headers={'Authorization': f'JWT {jwt}'})

print(response.status_code, response.json())
assert response.status_code == 200, 'Endpoint does not respond with 200'


