from abc import ABC, abstractmethod
from main.models import UserModel
from book.models import BookModel
class PaymentAbstract(ABC):
    """ abstract class to define a payment method to trade a book 
        1: process_payment (check permissions and validations, and confirm_payment if its all ok)
        2: confirmation_trade (att books status and/or  user points)
        3: finalizate_trade (confirm all instances status (trades and books), and display success tasks)
        4: cancel_payment (return all instances status, and delete the trade)
    """
    def __init__(self) -> None:
        ...

    @property
    @abstractmethod
    def trade_value(self):
        ...

    @abstractmethod
    def get_code(self):
        ...

    @abstractmethod
    def get_description(self):
        ... 

    @abstractmethod    
    def process_payment(self, *args, **kwargs):
        ...

    @abstractmethod
    def validate_payment(self, *args, **kwargs):
        ...

    def confirmation_payment(self, *args, **kwargs):
        ...

    def confirmation_trade(self, *args, **kwargs):
        ...
        
    def finalizate_payment(self, *args, **kwargs):
        ...

    def cancel_payment(self, *args, **kwargs):
        ...