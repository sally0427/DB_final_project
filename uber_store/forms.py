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


class addProductForm(forms.Form):
    Pname = forms.CharField(label='商品名稱', max_length=10)
    Pprice = forms.CharField(label='商品價錢', max_length=10)


class UploadModelForm(forms.ModelForm):
    image = forms.FileInput(attrs={'class': 'form-control-file'})
    class Meta:
        model = Store
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
