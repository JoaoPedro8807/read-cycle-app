from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError as DjangoValidationError
import re
from .base.user_base_model import BaseUserAbstract
from .manager.user_manager import UserManager
import os
from decimal import Decimal
from django.core.validators import FileExtensionValidator
from django.conf import settings
import random

def save_user_image(user, file_name):
    file_name = f'{user.last_name}-background.png'.replace(' ', '-')
    return os.path.join(f'user/images/{str(user.document)}', file_name)

def get_user_avatar_random():
    avatar_dir = os.path.join(settings.MEDIA_ROOT, 'users/avatars')
    avatars = [files for files in os.listdir(avatar_dir)]
    random_avatar = random.choice(avatars)
    random_with_path =  os.path.join(avatar_dir, random_avatar)
    print('RANDOM: ', random_with_path)
    return os.path.join(avatar_dir, random_avatar)  



class UserModel(AbstractBaseUser,  BaseUserAbstract, PermissionsMixin):
    """ rewrithen default user model from django, to add some new fields and data """ 

    objects = UserManager()
    email = models.EmailField(_("Email"), max_length=50, unique=True)
    points = models.DecimalField(_("Pontos"), default=Decimal(100), decimal_places=2, max_digits=6) # enough to make a request or trade a book. When trade a book, he nedded receive these points
    document = models.CharField(_("CPF"), max_length=50, unique=True)     #então o usuario pode tanto oferecer o livro dele em troca, ou então requisitar o livro em troca de pontos, aí o outro usuário recberá esses pontos
    phone_number = models.CharField(_("Telefone"), max_length=20)
    first_name = models.CharField(_("Nome"), max_length=50)
    last_name = models.CharField(_("Sobrenome"), max_length=50) 
    street = models.CharField(_("Rua"), max_length=100)
    number = models.CharField(_("Número"), max_length=20) 
    district = models.CharField(_("Bairro"), max_length=100, default='teste')
    city = models.CharField(_("Cidade"), max_length=100)
    state = models.CharField(_("Estado"), max_length=100)
    zip_code = models.CharField(_("CEP"), max_length=10)
    latitude = models.FloatField(_("latitude"), blank=True, null=True)
    longitude = models.FloatField(_("longitude"), blank=True, null=True)
    password = models.CharField(_("password"), max_length=100)
    image = models.ImageField(
        blank=True, 
        null=True, 
        default=get_user_avatar_random, 
        validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])    

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = 'user'

    def __str__(self) -> str:
        return f'{self.first_name} - ({self.email})'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def public_andress(self):
        return f'{self.city} - {self.state}'.capitalize()

    
    def add_points(self, value:Decimal = Decimal(100.00))-> None: #default book price to trade
        if value > 0:
            self.points += value
        return
    
    def sub_points(self, value: Decimal = Decimal(100.00)) -> None:
        if (self.points - value) >= 0:
            print('pontos antes:', self.points)
            self.points -= value
            print('pontos depois: ', self.points)
        return
    
    
    


