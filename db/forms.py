from django import forms
from .models import OilField


class FieldUpdateForm(forms.ModelForm):
    class Meta:
        model = OilField
        fields = ('name', 'type', 'location', 'owner', 'obzor_img')
        # exclude = []  # all fields
