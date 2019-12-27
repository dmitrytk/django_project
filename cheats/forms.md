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



