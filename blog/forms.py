from django import forms

def start_with_s(value):
      if value[0]!='s':
        raise forms.ValidationError("Name should start with s")

  
  
class StuForm(forms.Form):
  name = forms.CharField(
    validators =[start_with_s])