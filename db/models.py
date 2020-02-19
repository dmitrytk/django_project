from django.db import models
from django.urls import reverse


class OilField(models.Model):
    name = models.CharField(max_length=100, verbose_name='Oil field', unique=True)
    type = models.CharField(max_length=100, verbose_name='Type', blank=True)
    location = models.CharField(max_length=100, verbose_name='Location', blank=True)
    owner = models.CharField(max_length=100, verbose_name='Owner', blank=True)
    description = models.TextField(blank=True, verbose_name='Description')
    map = models.ImageField(blank=True, upload_to='maps', height_field=None, width_field=None, max_length=100,
                            verbose_name='Map')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):  # new
    #     return reverse('field_detail', args=[str(self.id)])


class Well(models.Model):
    name = models.CharField(max_length=100)
    field = models.ForeignKey(
        OilField, related_name='wells', on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True)
    alt = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True)
    md = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True)
    x = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True)
    y = models.DecimalField(
        max_digits=30, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('name', 'field',)

    def __str__(self):
        return self.name
