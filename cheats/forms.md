## Basic Django forms


Simple html form. action -> resource/url
```html
<form action="/team_name_url/" method="post">
    <label for="team_name">Enter name: </label>
    <input id="team_name" type="text" name="name_field" value="Default name for team.">
    <input type="submit" value="OK">
</form>
```

Django form class
```python
from django import forms
    
class OilFieldForm(forms.Form):
    name = forms.CharField(max_length=50,
         label='Oil field name',
         required=True,
        error_messages={'required': 'Please enter field name'})
    type = forms.CharField(max_length=50, initial='oil')
    owner = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
```

Manual validation. cleaned_data
```python
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        # Check if not in past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if not in future.
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Always return cleaned data
        return data
```






