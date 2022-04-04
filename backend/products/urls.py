from django.urls import path

from . import views
# from .views import get_products

urlpatterns = [
  # path('', views.get_products)
  path('', views.product_list_create_view),
  path('<int:pk>/update/', views.product_update_view ),
  path('<int:pk>/delete/', views.product_delete_view ),
  path('<int:pk>/', views.product_detail_view ),
  # path('', views.product_alt_view),
  # path('<int:pk>/', views.product_alt_view )
]