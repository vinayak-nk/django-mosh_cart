import requests


endpoint = 'http://httpbin.org/status/404'
endpoint = 'http://127.0.0.1:9000/api/'
response = requests.get(endpoint)

print(response.text)
print(response.status_code)
print(response.json())
