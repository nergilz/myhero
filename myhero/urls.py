from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('hero.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('hero.urls')),
]
