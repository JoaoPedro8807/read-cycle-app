from django.db import models
from django import template

register = template.Library()

@register.filter(name='unzip')
def is_object(zip_list: list, index:int):
    return [item[index] for item in zip_list] 

