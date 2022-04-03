
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product
# Create your views here.

@api_view(['GET', 'POST'])
def get_products(request, *args, **kwargs):
  """
  DRF API VIEW
  """
  if request.method == 'GET':
    instance = Product.objects.all().order_by("?").first() 
    data = {}
    if instance:
      data = ProductSerializer(instance).data
    return Response(data)
  else:
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      instance = serializer.save()
      print(instance)
      return Response(serializer.data)
    return Response({"invalid": "invalid data"}, status=400)
    


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
