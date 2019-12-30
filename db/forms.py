from django import forms


class FieldUpdateForm(forms.Form):
    name = forms.CharField(label='Oil field name', required=True,
                           error_messages={'required': 'Please enter field name'})
    type = forms.CharField()
    location = forms.CharField()
    owner = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    obzor_img = forms.ImageField()
