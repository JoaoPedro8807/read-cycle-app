from django import forms

#formulario com campos soltos, sem ser atrelado ao model
class LoginForm(forms.Form): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    email = forms.EmailField()
    password = forms.CharField( 
        required=True,
        widget=forms.PasswordInput()
    )

    email.widget.attrs['placeholder'] = 'Digite seu nome'
    password.widget.attrs['placeholder'] = 'Digite sua senha'