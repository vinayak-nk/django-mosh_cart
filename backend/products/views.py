from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product
# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  def perform_create(self,serializer):
    # print('*******', serializer.validated_data)
    cont = serializer.validated_data.get('content') or None
    if cont is None:
      cont = serializer.validated_data.get('title')
    serializer.save(content=cont)    
    #send django signal

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # lookup_field = 'pk'
  
product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.RetrieveAPIView):
  """ NOT USING THIS METHOD"""
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
product_list_view = ProductListAPIView.as_view()

# from django.http import JsonResponse
# from django.forms.models import model_to_dict

# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from .serializers import ProductSerializer
# from .models import Product
# # Create your views here.

# @api_view(['GET', 'POST'])
# def get_products(request, *args, **kwargs):
#   """
#   DRF API VIEW
#   """
#   if request.method == 'GET':
#     instance = Product.objects.all().order_by("?").first() 
#     data = {}
#     if instance:
#       data = ProductSerializer(instance).data
#     return Response(data)
#   else:
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       instance = serializer.save()
#       print(instance)
#       return Response(serializer.data)
#     return Response({"invalid": "invalid data"}, status=400)
    


# # @api_view(['GET'])
# # def get_products(request):
# #   """  DRF API VIEW """
# #   product = Product.objects.all().order_by("?").first()
 
# #   data = {}
  
# #   if product:
# #     # data = model_to_dict(product)
# #     data = model_to_dict(product, fields=['id', 'price'])
# #     # data['title'] = product.title
# #     # data['content'] = product.content
# #     # data['price'] = product.price
  
# #   # return JsonResponse(data)
# #   return Response(data)
