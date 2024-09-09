from django import forms
from ..models.shippings_methods_choice import get_all_shipping_methods_choice

class ShippingForm(forms.Form):
    
    method = forms.ChoiceField(
    label='Método de envio', 
    choices=get_all_shipping_methods_choice(), 
    required=True,
    widget=forms.Select(    
        attrs={
            'class': 'shipping_method_choice',
        }
    ))

    cod = forms.CharField(
        label='Código de postagem', 
        max_length=100, 
        required=True)


