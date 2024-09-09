from typing import Any
from ..models import AvaliationModel
from django import forms
from django.core.exceptions import ValidationError
from ..utils.form_default_value import add_attr



class AvaliationForm(forms.ModelForm):
    class Meta:
        model = AvaliationModel
        fields = [
            'rating',
            'title',
            'body',
        ]
