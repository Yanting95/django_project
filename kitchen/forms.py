from django.forms import ModelForm
from django import forms
from . models import Kitchen, Dish, Days


# DAYS_OF_WEEK = (
#     ('0', 'Monday'),
#     ('1', 'Tuesday'),
#     ('2', 'Wednesday'),
#     ('3', 'Thursday'),
#     ('4', 'Friday'),
#     ('5', 'Saturday'),
#     ('6', 'Sunday'),
# )


class KitchenForm(ModelForm):
    # widgets = {'day': forms.CheckboxSelectMultiple}
    # widgets = {'password': forms.PasswordInput}
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Kitchen
        fields = ('name', 'email', 'password', 'start_time', 'end_time', 'image')


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ('name', 'veg', 'description', 'price', 'image')


class DaysForm(ModelForm):
    class Meta:
        model = Days
        fields = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

