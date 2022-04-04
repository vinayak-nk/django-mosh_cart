from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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

class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  
  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title
  
product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  def perform_destro(self, instance):
    super().perform_destroy(instance)
  
product_delete_view = ProductDeleteAPIView.as_view()

class ProductListAPIView(generics.RetrieveAPIView):
  """ NOT USING THIS METHOD"""
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
product_list_view = ProductListAPIView.as_view()


class ProductMixinView(
  mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
  generics.GenericAPIView
  ):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  
  def get(self, request, *args, **kwargs):
    pk = kwargs.get('pk')
    if pk is not None:
      return self.retrieve(request, *args, **kwargs)
    return self.list(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def perform_create(self,serializer):
    cont = serializer.validated_data.get('content') or None
    if cont is None:
      cont = 'test content'
    serializer.save(content=cont)    


product_mixin_view = ProductMixinView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
  method = request.method
  
  if method == 'GET':
    if pk is None:
      queryset = Product.objects.all()
      data = ProductSerializer(queryset, many=True).data
      return Response(data)
    # Detail view part
    obj = get_object_or_404(Product, pk=pk)
    data = ProductSerializer(obj, many=False).data
    return Response(data)
  else: # POST
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      cont = serializer.validated_data.get('content') or None
      if cont is None:
        cont = serializer.validated_data.get('title')
      serializer.save(content=cont)    

      return Response(serializer.data)
    return Response({"invalid": "invalid data"}, status=400)



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
