from abc import ABC, abstractmethod


class ShippingAbstract(ABC):

    
    @abstractmethod
    def get_shipping_code(self):
        ...

    @abstractmethod
    def get_shipping_name(self):
        ...

    @abstractmethod
    def proccess_ship(self, *args, **kwargs):
        ...

    @abstractmethod
    def ship_confirmation(self, *args, **kwargs):
        ...

    @abstractmethod
    def finalizate_ship(*args, **kwargs):
        ...

    @abstractmethod
    def calculate_price_shipping(self, *args, **kwargs):
        ...

