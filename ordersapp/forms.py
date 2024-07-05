from django import forms
import datetime


class PictForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField()
    price = forms.IntegerField()
    quantity = forms.IntegerField()
    registration_date = forms.DateField(initial=datetime.date.today)
    image = forms.ImageField()
