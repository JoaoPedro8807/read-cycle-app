from django.db import models
from django import template

register = template.Library()

@register.filter(name='is_object')
def is_object(value):
    try:
        return isinstance(value, models.Model)

    except (ValueError, TypeError): 
        return False        