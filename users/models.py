from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    job = models.CharField(max_length=50, blank=True)
    profile_photo = models.ImageField(blank=True, upload_to='profile_photos', height_field=None, width_field=None, max_length=100,
                                      verbose_name='Profile photo')
