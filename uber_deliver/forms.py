from django import forms
from uber_deliver import models
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    Dname = forms.CharField(max_length=20)
    Dphone = forms.CharField(max_length=20)
    ValidationError('Invalid value')

    class Meta:
        model = models.Deliver
        fields = [
            'Dname',
            'Dphone'
        ]
