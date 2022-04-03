from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Product
# Create your views here.

def get_products(request):
  product = Product.objects.all().order_by("?").first()
 
  data = {}
  
  if product:
    # data = model_to_dict(product)
    data = model_to_dict(product, fields=['id', 'price'])
    # data['title'] = product.title
    # data['content'] = product.content
    # data['price'] = product.price
  
  return JsonResponse(data)