from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('steam/', include('steam.urls')),  # Incluindo as URLs do app Steam
]
