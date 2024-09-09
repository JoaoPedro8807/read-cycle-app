from . import CorreiosShipping, ShippingAbstract

class ShippingFacotry:
    _shipping_methods = {
        'CR': CorreiosShipping
    }


    @classmethod
    def register_shipping_instance(cls, method_key: str, method_class: type) -> None:
        if not issubclass(method_class, ShippingAbstract):
            raise ValueError('Classe deve ser da interface payment')
        cls._shipping_methods[method_key] = method_class

    @classmethod
    def get_shipping_instance(cls, method_key: str, *args, **kwargs) -> ShippingAbstract:
        method = cls._shipping_methods.get(method_key)
        if not method:                                                              
            raise ValueError('O method_key passado para a criação está errado')
        return method

    
    @property
    def all_methods(self):
        return self._shipping_method()
