from django import forms

from .models import OwnIngredient


class OwnIngredientForm(forms.ModelForm):
    class Meta:
        model = OwnIngredient
        fields = [
            'name'
        ]

