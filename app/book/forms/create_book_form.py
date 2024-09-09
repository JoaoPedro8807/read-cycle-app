from typing import Any
from ..models import BookModel
from django import forms
from django.core.exceptions import ValidationError
from ..utils.form_default_value import add_attr
from ..models import CategoryModel


class CreateBookForm(forms.ModelForm):
    def init(self, data, *args, **kwargs):
        self._post_data = data
        super().__init__(*args, **kwargs)

        add_attr(self.fields['title'], 'value', self.instance.title)
        add_attr(self.fields['authors'], 'value', self.instance.authors)
        add_attr(self.fields['version'], 'value', self.instance.version)
        add_attr(self.fields['description'], 'value', self.instance.description)
        add_attr(self.fields['published_at'], 'value', self.instance.published_at)
        add_attr(self.fields['total_pages'], 'value', self.instance.total_pages)
        add_attr(self.fields['language'], 'value', self.instance.language)

       

    #hiden inputs
    book_api_id = forms.CharField(
        required=False,
        label='',
        widget=forms.HiddenInput()
    )
    book_api_etag = forms.CharField(
        required=False,
        label='',
        widget=forms.HiddenInput()
    )
    image = forms.ImageField(
        label='',
        widget=forms.FileInput(
            attrs={'accept': 'image/jpg, image/jpeg, image/png'}
        ),
        required=False
    )
    


    class Meta: 
        model = BookModel
        fields = [
            'book_api_id',
            'book_api_etag',
            'title',              
            'category',                                                                      
            'authors',
            'version',
            'published_at',
            'description',  
            'total_pages',
            'language',
            'image'
        ]
        widgets = {
            'published_at': forms.DateInput(attrs={'type': 'date'}),
            }
            
    def save(self, commit: bool = True) -> Any:
        # sourcery skip: inline-immediately-returned-variable
        instance =  super().save(commit=commit) 
        return instance


    def clean(self) -> dict[str, Any]:
        # sourcery skip: inline-immediately-returned-variable
        cleaned_data =  super().clean()
        
        return cleaned_data