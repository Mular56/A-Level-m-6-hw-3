from django.urls import path
from customer.views import index, SignUpView, ProductListView, MyLoginView, personal_cabinet
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(template_name='login.html'), name='login'),
    path('products/', ProductListView.as_view(), name='products'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('personal_cabinet/', personal_cabinet, name='personal_cabinet'),
]