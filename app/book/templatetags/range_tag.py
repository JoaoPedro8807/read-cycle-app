from django import template


register = template.Library()


@register.filter(name='range_int')
def range_int(value: int):
    return range(value)                                                                                 