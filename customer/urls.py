from django.urls import path
from customer.views import index, SignUpView, ProductListView, MyLoginView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(template_name='login.html'), name='login'),
    path('products/', ProductListView.as_view(), name='products'),
]