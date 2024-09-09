from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from ..models import TradeModel, get_all_shipping_methods_choice


class CreateTradeForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        form = super().__init__(*args, **kwargs)

        self.fields['offer_book'] = forms.ChoiceField(
            label = 'Selecione um de seus livros',
            required=False,
            choices=[(book.id, book.title) for book in user.book.all()],
            widget=forms.Select(    
                attrs={
                    'class': 'user_books_option',
                }
            )   
        )

        self.fields['shipping_method'] = forms.ChoiceField(
            required=True,
            choices=get_all_shipping_methods_choice()
        )
    

    class Meta:
        model = TradeModel
        fields =  [
            'shipping_method',
            'payment_method',
        ]


