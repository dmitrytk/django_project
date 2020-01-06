from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),  # allauth
                  path('', include('pages.urls')),  # Home and tools pages
                  path('db/', include('db.urls')),  # Oil field and well database
                  path('accounts/', include('users.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
