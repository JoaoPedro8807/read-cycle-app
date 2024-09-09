from .payment import Payment, PaymentFactory
from main.models import UserModel
from .shipping import Shipping, ShippingFacotry
from .models import TradeModel

def zip_trade_payment_objects(trades: list,  user: UserModel) -> list:
    """ return a zip list with tuple (trade_object, {payment, shipping}) """
    payments = list(map(
        lambda trade: (
            trade,
            Payment(
                payment_method=PaymentFactory.create_payment_method(method_key=trade.payment_method),
                user=user,
                book=trade.book,
                trade=trade),
            Shipping(
                shipping=ShippingFacotry.get_shipping_instance(trade.shipping_method),
                _from=format_shipping_params(trade=trade, user=user)['_from'],
                _to=format_shipping_params(trade=trade, user=user)['_to']
            )
        ),
        trades
    ))
    return payments

def format_shipping_params(trade: TradeModel, user: UserModel) -> dict: 
    shipping_cal = {
        '_from': trade.book.owner.zip_code,
        '_to': trade.user.zip_code
    }
    if user == trade.user: # o frete pode mudar de preço dependendo da ordem dos ceps
        shipping_cal['_from'], shipping_cal['_to'] = shipping_cal['_to'], shipping_cal['_from']
    return shipping_cal



