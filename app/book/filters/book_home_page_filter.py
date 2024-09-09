import django_filters 
from ..models import BookModel
from django import forms 
from django.db.models import Q
from django.db.models.functions import Abs
from django.db.models import F

class BookHomeFilter(django_filters.FilterSet):
    language = django_filters.MultipleChoiceFilter(
        choices=(
            ('pt-BR', 'Português'),
            ('en', 'Inglês')
        ),
        label='Idiomas',
        widget=forms.CheckboxSelectMultiple()
    )
    proximidade = django_filters.CharFilter(
        method='filter_by_loc',
        field_name='Livros próximos',
        label='Livros próximos',
        widget=forms.CheckboxInput()
    )

    search = django_filters.CharFilter( #the search box to search for title or authors
        method='filter_by_all', 
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Pesquisa por livros',
            'maxlength': 100
        })
        ) 
            
    class Meta:
        model = BookModel
        fields = [
            'category',
            'language',
        ]


    def filter_by_all(self, queryset, name, value):
        return queryset.filter(
            Q(title__istartswith=value) | Q(authors__istartswith=value)
        )
    
    def filter_by_loc(self, queryset, name, value):
        print('VALUE DO FILTER: ', value)
        return queryset
        # else:
        #     print('NÃO VEIO VALUE NO FILTER', value)
