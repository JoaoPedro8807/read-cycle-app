# signals.py
from trade.shipping import ShippingFacotry, Shipping
from trade.models import TradeBaseModel
from typing import Type, Union

def get_shipping_method(trade: TradeBaseModel) -> Shipping:

    shipping_method = ShippingFacotry.get_shipping_instance(
    method_key=trade.shipping_method)

    shipping = Shipping(
            shipping=shipping_method, 
            _from=trade.book.owner.zip_code,
            _to=trade.user.zip_code
        )
    
    return shipping
    

    



