from typing import Any
from django.contrib.auth.models import BaseUserManager
from django.db import IntegrityError, OperationalError
from django.core.exceptions import ValidationError as DjangoValidationError

class UserManager(BaseUserManager):
    """
    centralizes user creation for authentication and user
    """
    def create_user(
            self, 
            email: str, 
            password: str,  
            username:str, 
            extra_fields: dict, 
            is_active:bool = True,
            ):
        email = self.normalize_email(email)
        print('DATA INDO PRO CREATE: ', extra_fields)
        try:
            user = self.model(
                email=email,                                                                                        
                username=username,
                password=password,
                is_active=is_active,
                **extra_fields
                )   
            user.full_clean()
            user.set_password(password)
            user.save(using=self._db)
            print('USUÁRIO CRIADO: ', user)
        except (ValueError, IntegrityError) as e:
            raise DjangoValidationError({'detail': f'Dados inccoretos: {str(e)}'}) from e

        except Exception as e:
            print('Erro ao criar UserAuth: ', e)
            raise DjangoValidationError({'detail': f'Erro ao criar usuário: {e}'}) from e   

        return user
        
    def create(self, **kwargs: Any) -> Any:
        return self.create_user(**kwargs)
        #return super().create(**kwargs)
    
    def create_superuser(self, email:str, password:str, username:str,  **extra_fields):
        print('VALORES DOE EXTRA_FIELDS: ', extra_fields)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        print('VALORES DOE EXTRA_FIELDS DEPOIS: ', extra_fields)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Para criar super usuário, ele deve ser definido como is_staff primeiro ')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Para criar um superuser ele deve ser definido como issuperuser primeiro.')

        return self.create_user(email=email, password=password, username=username, extra_fields=extra_fields)
    

