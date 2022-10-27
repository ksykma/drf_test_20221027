from rest_framework_simplejwt.views import ( 
    TokenObtainPairView, 
    TokenRefreshView, 
) 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='...'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='...'),
]

