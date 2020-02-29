from django.db import models
from django.urls import reverse


class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(max_length=254, verbose_name='Email')
    message = models.TextField(verbose_name='Messages')
    unread = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]
