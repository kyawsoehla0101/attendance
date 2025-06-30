from django import forms
from .models import PersonProfile

class PersonForm(forms.ModelForm):
    class Meta:
        model = PersonProfile
        fields = ['name',  'reg_no']