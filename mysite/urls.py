from books.views import view_base, view1, view2, view3, view4, view5, view6
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('base/', view_base, name='base_page'),
    path('created/', view1, name='create_comments'),
    path('latest/', view2, name='latest_comments'),
    path('text/', view3, name='latest_text'),
    path('updated/', view4, name='special_comments'),
    path('delete/', view5, name='delete_comments'),
    path('view6/', view6, name='latest_article_comments'),
    
    
]
