from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # allauth urls
    path('', include('home.urls')),  # Home page
    path('tools/', include('tools.urls')),  # Static tool pages
    path('db/', include('db.urls')),  # Oil field database
]
