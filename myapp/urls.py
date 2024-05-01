from django.urls import path
from .views import check_eligibility, home_view, login_view, \
    logout_view, register, welcome, change_password_view, \
        search_comments

urlpatterns = [
    path('', home_view, name='home_view'),
    path('check_eligibility/', check_eligibility, name='check_eligibility'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('welcome/', welcome, name='welcome'),
    path('change-password/', change_password_view, name='change_password'),
    path('search_comments/', search_comments, name='search_comments'),
    
]