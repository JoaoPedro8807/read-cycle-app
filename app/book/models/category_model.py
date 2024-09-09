from .base.book_base_model import BookBaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
import os


class CategoryModel(BookBaseModel):
    name = models.CharField(_("nome"), max_length=50)
    slug = models.SlugField(_("categoria"))


    
    class Meta:
        verbose_name = _("categoria")
        verbose_name_plural = _("categorias")
        db_table = 'categoria'    


    def __str__(self) -> str:
        return self.name
    
