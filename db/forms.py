from django import forms
from .models import OilField


class FieldUpdateForm(forms.ModelForm):
    class Meta:
        model = OilField
        fields = ('name', 'type', 'location', 'owner', 'map')
        # exclude = []  # all fields
