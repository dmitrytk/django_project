from django import forms
from .models import OilField, Well


class FieldUpdateForm(forms.ModelForm):
    class Meta:
        model = OilField
        fields = ('name', 'type', 'location', 'owner', 'map', 'description')
        # exclude = []  # all fields


class FieldCreateForm(forms.ModelForm):
    class Meta:
        model = OilField
        fields = ('name', 'type', 'location', 'owner', 'map', 'description')


class WellCreateForm(forms.ModelForm):
    class Meta:
        model = Well
        # fields = ('name', 'field', 'type', 'alt', 'md', 'x', 'y')
        exclude = []  # all fields
