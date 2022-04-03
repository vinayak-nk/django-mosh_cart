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



print(response.status_code)
print(response.json())
