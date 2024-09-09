from .interface.shiping_interface import ShippingAbstract
from main.models import UserModel
from book.models import BookModel
class Shipping(ShippingAbstract):
    def __init__(
            self, 
            shipping: ShippingAbstract,
            _from: str,
            _to: str,
            *args, **kwargs
            ) -> None:
        self.shipping = shipping(_from=_from,  _to=_to, *args, **kwargs)
    
    def get_shipping_code(self):
        return self.shipping.get_shipping_code()
    
    def get_shipping_name(self):
        return self.shipping.get_shipping_name()

    def ship(self, *args, **kwargs):
        return self.shipping.ship(*args, **kwargs)
    
    def proccess_ship(self, *args, **kwargs):
        return self.shipping.proccess_ship(*args, **kwargs)
    
    def ship_confirmation(self, *args, **kwargs):
        return self.shipping.ship_confirmation(*args, **kwargs)
    
    def finalizate_ship(self, *args, **kwargs):
        return self.shipping.finalizate_ship(*args, **kwargs)
    
    def calculate_price_shipping(self, *args, **kwargs):
        return self.shipping.calculate_price_shipping(*args, **kwargs)
