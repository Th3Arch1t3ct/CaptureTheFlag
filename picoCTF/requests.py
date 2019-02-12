#!/usr/bin/env python3
import requests
import json
# JavaScript Object Notation

url = '10.15.0.77'

r = requests.get(url)
print(r.status_code)
print(r.text)

r = requests.get(url)
r = requests.put(url)
r = requests.delete(url)
r = requests.post(url)
r = requests.head(url)
r = requests.options(url)

# Custom data/headers must be passed through JSON
data = {'variable_name':'data'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(data), headers=headers)

r.headers['content-type'] = 'application/json; charset=utf-8'


# Add user
url = '10.5.0.85:5000/'
handle = 'arch1t3ct'
message = 'C3T{Pyth0n_R3qu3st$_4R3_eZ}'
passwd = 'noonewilleverguessthis'
data = {'password':passwd}
r = requests.post(url+handle, data=json.dumps(data)) # Create a User
r = requests.get(url +handle) # Get users page
data = {username, password, message}
r = requests.put()

data = {'password':passwd, 'message':message}
r = requests.put(url+handle, data=json.dumps(data))
