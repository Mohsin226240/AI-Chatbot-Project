from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatapp.urls')),  # chatapp ke urls ko include kiya
]
