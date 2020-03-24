import requests
import json

jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImNyaXN0aW5hZ2FyYnV6QGdtYWlsLmNvbSIsImV4cCI6MTU4NTY1OTg3OS4wLCJvcmlnX2lhdCI6MTU4NTA1NTA3OSwidXNlcl9pZCI6MzA1NjksInVzZXJuYW1lIjoiMTk5MzA4MjMzNDYwIiwidXNlcl9yb2xlIjoiY29uc3VtZXIifQ.2Dae-RnHfzeOpP6FWFOQCYHGisxn977j3D2FwBOOQEA'

response = requests.post('https://www.homeq.se/api/v1/user/applications', data=json.dumps({

}), headers={'Content-Type': 'application/json',
             'Authorization': f'JWT {jwt}'})


print(response.status_code, response.content)
