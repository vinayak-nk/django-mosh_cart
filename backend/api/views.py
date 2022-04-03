from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

# Create your views here.

def api_home(request, *args, **kwargs):
  return JsonResponse({
    'message': 'hellowwww'
  })