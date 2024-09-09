from typing import Any
from django.db import models
from django.db import IntegrityError, OperationalError
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db.models import Q

class TradeManager(models.Manager):
    def trades_unfinished(self, *args, **kwargs):
        return self.filter(
            status="OP"
        ).select_related('book', 'user').all()  
    
    def trades_accepted(self, *args, **kwargs):
        return self.filter(
            accepted=True
        ).select_related('book', 'user').all()  

    def trades_finished(self, *args, **kwargs): #query to get trade finalizete or trade with first_shipping (that waiting other user.shipping to be finalizated)
        return self.filter(
            Q(status="FN") | Q(status="FS") 
        ).select_related('book', 'user').all()
    
    def all_trades(self, *args, **kwargs):
        return self.select_related(
            'book', 'user'
        ).all().order_by('-created_at')
    
    def user_trades_requests(self, user, *args, **kwargs):
        return self.filter(
            Q(book__owner=user) | Q(user=user)
        ).select_related('book', 'user').all().order_by('-created_at')

