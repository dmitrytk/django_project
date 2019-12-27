from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render

from .models import OilField


class FieldView(ListView):
    model = OilField
    template_name = 'db/fields.html'
    context_object_name = 'fields'


class DetailFieldView(DetailView):
    model = OilField
    template_name = 'db/field_detail.html'
    context_object_name = 'field'
