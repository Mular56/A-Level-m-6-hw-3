from django.urls import path, include
from customer.views import index, SignUpView, ProductListView, MyLoginView, personal_cabinet, \
    CustomerViewSet, UserViewSet, ProductViewSet, OrderViewSet
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(template_name='login.html'), name='login'),
    path('products/', ProductListView.as_view(), name='products'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('personal_cabinet/', personal_cabinet, name='personal_cabinet'),
    
    path('api/', include(router.urls)),
]