from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('', include('hero.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('hero.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token ),
]
