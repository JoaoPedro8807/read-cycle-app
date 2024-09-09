from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from ..models import UserModel
from book.utils import add_attr

class UserInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)


        for field in self.fields.values():
            field.required = False
            

    class Meta:
        model = UserModel
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'street',
            'number',
            'district',
            'city',
            'state',
            'zip_code'
        ]
    
    