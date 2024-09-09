from .interface.payment_interface import PaymentAbstract
from .book_method_payment import BookTradePayment
from .points_method_payment import PointsTradePayment

class PaymentFactory:
    """ simple factory to create a payment_method object """
    _paiment_methods = {
        'BT': BookTradePayment,
        'PT': PointsTradePayment
    }

    @classmethod
    def register_payment_method(cls, method_key: str, method_class: type):
        if not issubclass(method_class, PaymentAbstract):
            raise ValueError('Classe deve ser da interface payment')
        cls._paiment_methods[method_key] = method_class

    @classmethod
    def create_payment_method(cls, method_key: str, *args, **kwargs) -> PaymentAbstract:
        method = cls._paiment_methods[method_key]
        if not method:
            raise ValueError('O method_key passado para a criação está errado')
        return method

    
    @property
    def all_methods(self):
        return self._paiment_methods()
