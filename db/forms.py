from django import forms
from .models import OilField


class FieldUpdateForm(forms.ModelForm):
    class Meta:
        # fields = ['name', 'type', 'location'] select fields
        exclude = []  # all fields
        model = OilField
