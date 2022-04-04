import requests


###################################
# detail
###################################
endpoint = 'http://127.0.0.1:9000/api/products/1/'
# response = requests.get(endpoint)

###################################
# create
###################################

data = {
  "title": "new title123",
  "price": 100,
}
endpoint = 'http://127.0.0.1:9000/api/products/'
# response = requests.post(endpoint, json=data) # CREATE, POST
response = requests.get(endpoint) #LIST, get

###################################
# update
###################################
data = {
  "title": "new title hello",
  "price": 100,
}
endpoint = 'http://127.0.0.1:9000/api/products/1/update/'
response = requests.put(endpoint, json=data) #UPDATE, PUT

print(response.json())

###################################
# delete
###################################
endpoint = 'http://127.0.0.1:9000/api/products/10/delete/'
response = requests.delete(endpoint) #DELETE

print(response.status_code, "--", response.status_code == 204)
