from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('admin_views/', include('admin_panel.urls')),
    path('transactions/', include('transactions.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
