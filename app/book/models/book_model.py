from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
import os
from .base.book_base_model import BookBaseModel
from .base.book_manager import BookManager 
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def get_upload_path_image(instance: BookBaseModel, file_name:str)-> str:
    file_name = f'{instance.title}-background.png'.replace(' ', '-')
    return os.path.join(f'book/images/{str(instance.owner.document)}', file_name) #path to book image

class BookModel(BookBaseModel):
    owner = models.ForeignKey("main.UserModel", verbose_name=_("book"), on_delete=models.CASCADE, related_name='book')
    category = models.ForeignKey("book.CategoryModel", verbose_name=_("categoria"), on_delete=models.CASCADE, related_name='category')
    title = models.CharField(_("título"), max_length=100)
    authors = models.CharField(_("autor"), max_length=100)
    version = models.CharField(_("edição"), max_length=50)
    published_at = models.CharField(_("data de publicação"))
    language = models.CharField(_("idioma"), max_length=5)
    description = models.TextField(_("descricao"), max_length=10000)
    image = models.ImageField(upload_to=get_upload_path_image, blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])    
    available = models.BooleanField(_("disponibilidade"), default=True) 
    total_pages = models.IntegerField(_("número de paginas"))
    book_api_id = models.CharField(_("google api id"), max_length=50, blank=True) #google api id
    book_api_etag = models.CharField(_("google api tag"), max_length=50, blank=True)
    price = models.DecimalField(_("preço"), max_digits=5, decimal_places=2, null=True, blank=True, default=settings.DEFAULT_ANY_BOOK_PRICE)

    objects = BookManager()

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")
        db_table = 'book'    


    def __str__(self) -> str:
        return f'{self.title} - {self.authors} - {self.language}'



    def att_available_status(self, status:bool) -> bool:
        self.available = status
        self.save()


    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: list[str] | None = ...) -> None:
        if self.image:
            width = int(settings.DEFAULT_PX_WIDTH_BOOK_IMAGE)
            heigth = int(settings.DEFAULT_PX_HEIGTH_BOOK_IMAGE)
            img = Image.open(self.image)
            img = img.resize((width, heigth), Image.Resampling.LANCZOS)

            img_io = BytesIO()  #deixa o resize em io, e dps sobreescreve no /media 
            img.save(img_io, format=img.format or 'png')
            self.image.save(
                name=self.image.name,
                content=ContentFile(img_io.getvalue()),
                save=False)

        save = super().save()
        return save
