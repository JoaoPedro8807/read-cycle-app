from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from ..manger import TradeManager
from django.conf import settings

class TradeBaseModel(models.Model):

    def get_status_choices(*args, **kwargs):
        return [ 
            ("OP", "Aberta"),
            ("AC", "Aceita"),           
            ("FS", "Aguarda envio"),
            ("FN", "Finalizada" ),
            ("CN", "Cancelada")
        ]         
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True, editable=False)
    accepted = models.BooleanField(_("status"), default=False) #True if Trade is accept to above users, else false
    finalizate = models.BooleanField(_("finalizado"), default=False)
    status = models.CharField(choices=settings.TRADE_STATUS_FLAGS or get_status_choices(), default="OP", max_length=2)




    class Meta:
        abstract = True
        ordering = ['-created_at']



