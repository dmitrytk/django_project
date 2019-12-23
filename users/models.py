from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    job = models.CharField(max_length=50, blank=True)
