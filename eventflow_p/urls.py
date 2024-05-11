from django.urls import path, include
from django.contrib import admin
from events import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', include('events.urls')),
    path('admin/', admin.site.urls),  
]
