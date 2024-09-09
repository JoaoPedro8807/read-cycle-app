from typing import Iterable
from django.db import models
from .payments_methods_choice import get_all_choice_payment_methods
from .shippings_methods_choice import get_all_shipping_methods_choice
from django.utils.translation import gettext_lazy as _
from .base.trade_base_model import TradeBaseModel
from .manger import TradeManager    
from decimal import Decimal



class TradeModel(TradeBaseModel):
    book = models.ForeignKey("book.BookModel", verbose_name=_("livro"), on_delete=models.CASCADE, related_name='trade')
    user = models.ForeignKey("main.UserModel", verbose_name=_("usuário"), on_delete=models.CASCADE, related_name='trades')
    payment_method = models.CharField(choices=get_all_choice_payment_methods(), verbose_name=_("Método de pagamento"))
    shipping_method = models.CharField(choices=get_all_shipping_methods_choice(), verbose_name=_("Método de envio"), null=True, blank=True)

    book_offer = models.ForeignKey("book.BookModel", verbose_name=_('livro ofertado'), on_delete=models.CASCADE, related_name='offers', null=True, blank=True)
    points_offer = models.DecimalField(verbose_name=_('pontos ofertados'), max_digits=6, decimal_places=2, null=True, blank=True, default=Decimal(100))

    first_ship = models.BooleanField(_("Primeiro envio"), default=False, null=True, blank=True)
    user_shipping_code = models.CharField(_("Código de envio do requisitante"), null=True, blank=True, max_length=20,) #unique=True)
    owner_shipping_code = models.CharField(_("Código de envio do propietário"), null=True, blank=True, max_length=20,) #unique=True)


    objects = TradeManager()

    class Meta:
        verbose_name = _("trade")
        verbose_name_plural = _("trades")
        db_table = 'trades'

    def __str__(self):
        return f'{self.book}, por {self.user} ({self.payment_method})'

    # def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
    #     # if self.points_offer:
    #     #     self.points_offer = Decimal(self.points_offer)
    #     return super().save()

