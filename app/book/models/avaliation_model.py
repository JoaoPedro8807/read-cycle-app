from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
import os
from .base.book_base_model import BookBaseModel


class AvaliationModel(BookBaseModel):
    user = models.ForeignKey("main.UserModel", verbose_name=_("usuario"), related_name="user_avaliations", on_delete=models.CASCADE)  
    post = models.ForeignKey("book.BookModel", verbose_name=_("post"), related_name='avaliations', on_delete=models.CASCADE)
    title = models.CharField(_("titulo"), max_length=50)   
    rating = models.IntegerField(_("nota"), choices=[(i, i) for i in range(1, 6)], blank=True, null=True)
    body = models.TextField(_("Comentário"))

    class Meta:
        verbose_name = _("avaliacao")
        verbose_name_plural = _("avaliacoes")
        db_table = 'avaliacao'    

    def __str__(self) -> str:
        return f'{self.user} - {self.title}'
