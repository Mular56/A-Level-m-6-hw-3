from django.urls import path
from .views import AdminProductListView, AdminProductCreateView, AdminProductUpdateView

urlpatterns = [
    path('products/', AdminProductListView.as_view(), name='admin_products'),
    path('products/add/', AdminProductCreateView.as_view(), name='admin_product_add'),
    path('products/edit/<int:pk>/', AdminProductUpdateView.as_view(), name='admin_product_edit'),
]
