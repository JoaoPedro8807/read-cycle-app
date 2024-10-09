# signals.py
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import task_send_email_new_trade, task_send_atualization_email
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from .models import TradeModel
from .services import get_payment_method, get_shipping_method
from celery import group

@receiver(post_save, sender=TradeModel)
def send_email_new_trade(sender, instance, created, **kwargs) -> None:
    """ catch the signal from TradeModel on post_save, and send email confirmation to book.owner and trade.user """
    if created:
        try:
            payment = get_payment_method(trade=instance)

            shipping = get_shipping_method(trade=instance)
            shipping_estimate_price = shipping.calculate_price_shipping()
            
            book = instance.book

            task_send_email_new_trade.delay(
                email=book.owner.email,
                user_name=book.owner.full_name,
                request_owner_name = instance.user.full_name,
                book_to_trade=instance.book.title,
                payment_value=payment.trade_value,
                estimate_price = shipping_estimate_price,
            )
            
        except ObjectDoesNotExist as error:
            print('erro ao pegar o objeto no signals: ', error)

        except Exception as error:
            print('error no signals: ', error)

    return None

@receiver(post_save, sender=TradeModel)
def send_att_trade_email(sender, instance, created, **kwargs) -> None:
    """ send for all users, trade atualizations for any changes to trade"""
    print('INICIANDO O ATT TRADE_EMAIL')
    if not created: #to atuliations
        try:
            payment = get_payment_method(trade=instance)

            #send email for above users
            emails = [instance.user.email, instance.book.owner.email]
            emails_data = {
                'user_name': instance.book.owner.full_name,
                'request_owner_name': instance.user.full_name,
                'book_to_trade': instance.book.title,
                'payment_value': payment.trade_value,
                'trade_status': instance.status,
                'created_at': instance.created_at,
            }
            datas: list[dict] = []

            for email in emails:
                data = emails_data.copy()
                data['email'] = str(email)
                datas.append(data)

            #sending tasks in paralele execution with celery grop
            paralele_tasks = group(task_send_atualization_email.s(**data) for data in datas) 
            paralele_tasks.delay()
        

        except ObjectDoesNotExist as error:
            print('erro ao pegar o objeto no signals: ', error)

        except Exception as error:
            print('error no signals: ', error)

    return None