from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address', label='email')
    ValidationError('Invalid value')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'phone',
            'address'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(label='Email address', max_length=10)
    password = forms.CharField(label='password', widget=forms.PasswordInput())

# class addOrderGoodsForm(forms.Form):
#     Pid = forms.CharField(label='商品ID', max_length=10)
#     Pcount = forms.CharField(label='商品數量', max_length=10)
