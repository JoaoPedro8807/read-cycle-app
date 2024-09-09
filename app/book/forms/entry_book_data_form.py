from typing import Any
from ..models import BookModel
from django import forms
from django.core.exceptions import ValidationError


class EntryBookDataForm(forms.Form):
    title = forms.CharField(
        label='Título',
        required=True,
        error_messages={
            'required': 'O título é obrigatório',
            'teste_error': 'Testando msg de error do input'
        },
        widget=forms.TextInput({
                'placeholder': 'Digite o título do livro'
            }
        ),
        max_length=100
    )   

    authors = forms.CharField(
        label='Autor',
        required=True,
        error_messages={
            'required': 'O autor é obrigatório',
        },
        widget=forms.TextInput({
            'placeholder': 'Digite o nome do autor'
            }
        )
    )
    version = forms.CharField(
        label='Versão',
        required=True,
        error_messages={
            'required': 'A versão do livro é obrigatória',
        },
        widget=forms.TextInput({
            'placeholder': 'versão do livro'
            }
        )
    )
    published_at = forms.DateField(
        label='Data de publicação',
        required=False,
        error_messages={
            'invalid': 'Digite uma data válida'
        },
        widget=forms.DateInput(attrs={
            'type': 'date'
        })
        )

    class Meta: 
        fields = [
            'title',
            'authors',
            'version',
            'published_at',
        ]
            
    def clean_title(self):
        title = self.cleaned_data['title']
        print('clean_title chamado')

        return title

        

    def clean(self) -> dict[str, Any]:
        # sourcery skip: inline-immediately-returned-variable
        cleaned_data =  super().clean()
        
        return cleaned_data