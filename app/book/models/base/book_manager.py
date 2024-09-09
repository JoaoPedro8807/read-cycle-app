from typing import Any
from django.db import models
from django.db import IntegrityError, OperationalError
from django.core.exceptions import ValidationError as DjangoValidationError

class BookManager(models.Manager):
    """
    A book model manager
    """
    def books_available(self, *args, **kwargs):
        return self.filter(
            available=True
        )
    
    def all_books(self, *args, **kwargs):
        return self.all().select_related('owner', 'category')
    
    def users_books(self, user, *args, **kwargs):
        return self.filter(
            owner=user
        ).all().select_related('owner', 'category')