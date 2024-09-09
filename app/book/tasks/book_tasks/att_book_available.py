
from django.conf import settings
from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
from book.models import BookModel

 
logger = get_task_logger(__name__)
 
@shared_task()
def thirty_second_func(): #testando
    logger.info("I run every 30 seconds using Celery Beat")
    return "Done"
 

@shared_task(bind=True) 
def att_book_status(self, book:BookModel, status:bool,  *args, **kwargs):    
    #por enquanto deixei direto no process_payment
    return "Done"   
