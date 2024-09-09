from django.db import models
import uuid
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseUserAbstract(models.Model):
    """
    A abstract base model to default auth model rewrithen
    """
    id = models.BigAutoField(primary_key=True, editable=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)
    is_staff = models.BooleanField(_("staff user field"), default=False)
    is_active = models.BooleanField(_("active bool field"), default=True)
    is_superuser = models.BooleanField(_("super user field"), default=False)


    class Meta:
        abstract = True
        ordering = ['-created_at']


