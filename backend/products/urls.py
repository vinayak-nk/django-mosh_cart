from django.urls import path

from . import views
# from .views import get_products

urlpatterns = [
  # path('', views.get_products)
  path('<int:pk>/', views.ProductDetailAPIView.as_view())
]