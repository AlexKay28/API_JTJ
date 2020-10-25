# importing the requests library 
import requests 
import json
  
# use this adress and port
URL = "http://0.0.0.0:8085/solve"

# inputs
calc_id = input('Input calc id: ')
ar = [int(i) for i in input('input array in single line (ex 1 2 3): ').split(' ')]

# prepare to  make request
payload = {'calc_id': calc_id, 'elements': ar} 
headers = {'content-type': 'application/json'}

# lets do this!
response = requests.post(URL, data=json.dumps(payload), headers=headers)

# print putput 
print(response.status_code, response.json())