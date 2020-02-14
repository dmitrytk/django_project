from django.urls import path
from .views import profile_edit, profile

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]
