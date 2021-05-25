from django import forms
from uber_store.models import Store
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    Ｓname = forms.CharField(max_length=20)
    Ｓaddress = forms.CharField(max_length=120)
    Sphone = forms.CharField(max_length=20)
    ValidationError('Invalid value')

    class Meta:
        model = Store
        fields = [
            'Sname',
            'Saddress',
            'Sphone'
        ]
