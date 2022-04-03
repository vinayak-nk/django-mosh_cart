
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product
# Create your views here.

@api_view(['GET'])
def get_products(request, *args, **kwargs):
  """
  DRF API VIEW
  """
  instance = Product.objects.all().order_by("?").first() 
  data = {}
  if instance:
    data = ProductSerializer(instance).data
  return Response(data)


# @api_view(['GET'])
# def get_products(request):
#   """  DRF API VIEW """
#   product = Product.objects.all().order_by("?").first()
 
#   data = {}
  
#   if product:
#     # data = model_to_dict(product)
#     data = model_to_dict(product, fields=['id', 'price'])
#     # data['title'] = product.title
#     # data['content'] = product.content
#     # data['price'] = product.price
  
#   # return JsonResponse(data)
#   return Response(data)
