from django import forms
from .models import Treasure


# class TreasureForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     value = forms.DecimalField(label='Value', max_digits=10, decimal_places=2)
#     material = forms.CharField(label='Material', max_length=100)
#     location = forms.CharField(label='Location', max_length=100)
#     img_url = forms.CharField(label='image URL', max_length=255)

class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ['name', 'value', 'material', 'location', 'image']


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())