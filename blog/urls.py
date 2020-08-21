
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mooblog.urls')),
    path('menbers/', include('django.contrib.auth.urls')),
    path('menbers/', include('menbers.urls')),
]
