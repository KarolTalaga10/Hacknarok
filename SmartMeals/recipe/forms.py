from django import forms

from .models import OwnIngredient, Time


class OwnIngredientForm(forms.ModelForm):
    class Meta:
        model = OwnIngredient
        fields = [
            'name'
        ]

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = [
            'mins'
        ]
