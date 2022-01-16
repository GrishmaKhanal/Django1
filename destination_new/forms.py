from django import forms
from django.db.models import fields
from .models import *

class destform(forms.ModelForm):
    class Meta:
        model = airport
        # fields = ['a_name', 'a_location', 'a_image']
        fields = '__all__'
# image ko directory chalirako xaina
