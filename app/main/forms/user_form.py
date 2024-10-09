from typing import Any
from django import forms
from ..models import UserModel
from django.core.exceptions import ValidationError as DjangoValidationError


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'first_name',
            'last_name',
            'email', 
            'document',
            'phone_number',
            'street',
            'number',
            'district',
            'city',  
            'state',
            'zip_code',
            'password', 
            ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input w-100'}),
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)   
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
    def clean(self) -> dict[str, Any]:
        cleaned_data =  super().clean()
        if cleaned_data['first_name'] == 'teste':
            raise DjangoValidationError('Username não pode ser "teste".')

        return cleaned_data