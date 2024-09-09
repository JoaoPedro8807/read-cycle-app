from django.db import models
import uuid
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BookBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True, editable=False,)
                                                                                                                                                                                            

    class Meta:
        abstract = True 
        ordering = ['-created_at']


