from datetime import datetime, timedelta
from django import template

register = template.Library()

@register.filter(name='expired_trade_date')
def expired_trade_date(date) -> str:
    """ calc date when trade is expired  """
    expired_date = date + timedelta(days=7)
    current = datetime.now().date()
    return (expired_date - current).days


