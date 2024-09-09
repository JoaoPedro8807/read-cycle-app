from django import forms
from ..models import UserModel

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