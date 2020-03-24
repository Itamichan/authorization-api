import requests
import json

host = 'https://authorization-api-cristina.herokuapp.com/'

response = requests.post(f"{host}api/v1/registration", data=json.dumps({
    'username': 'alex',
    'password': 'helooo23,',
    'email': 'ana25@gmail.com'
}), headers={'Content-Type': 'application/json'})

print(response.status_code, response.json())
assert response.status_code == 200, 'Endpoint does not respond with 200'



