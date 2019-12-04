from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('tools/', include('tools.urls')),
    path('db/', include('db.urls')),
]
