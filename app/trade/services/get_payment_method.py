# signals.py
from trade.payment import Payment, PaymentFactory
from trade.models import TradeBaseModel
from typing import Type, Union

def get_payment_method(trade: TradeBaseModel) -> Payment:

    payment_method = PaymentFactory.create_payment_method(
    method_key=trade.payment_method)

    payment = Payment(
        payment_method=payment_method,
        user=trade.user,
        book=trade.book,
        trade=trade)
    
    return payment
    

    



