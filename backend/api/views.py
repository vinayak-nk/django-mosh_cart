import json
from django.http import JsonResponse

# Create your views here.

def api_home(request, *args, **kwargs):
  data = {}
  try:
    data = json.loads(request.body) #string of json data --> python dict
    data['content_type'] = request.content_type
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
  except:
    pass
  print(f'data={data}')
  # print(f'params', request.GET)
  # print(request.headers)
  return JsonResponse(data)
