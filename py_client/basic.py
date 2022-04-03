import requests


endpoint = 'http://httpbin.org/status/404'
endpoint = 'http://127.0.0.1:9000/products/'


response = requests.get(endpoint, params={'abc': 123}, json={'query': 'hi! hellow'})
response = requests.post(endpoint, json={'product_id': 123, 'title': None})
response = requests.post(endpoint, json={'title': 'test'})

# print(response.text)
print(response.status_code)
print(response.json())
