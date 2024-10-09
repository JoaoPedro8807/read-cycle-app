import os
from .interface.shiping_interface import ShippingAbstract
from .correios_services import fetch_tracking_data
import requests

class CorreiosShipping(ShippingAbstract):
    def __init__(self, post_code:str = None, _from:str=None, _to:str=None, *args, **kwargs) -> None:
        self.post_code = post_code,
        self._from = _from or kwargs.get('_from'),
        self._to = _to or kwargs.get('_to')


    def get_shipping_code(self):
        return "CR"
    
    def get_shipping_name(self):
        return "Correios"

    def proccess_ship(self, *args, **kwargs):
        self.ship_confirmation(*args, **kwargs)
        self.finalizate_ship(*args, **kwargs)

    def ship_confirmation(self, *args, **kwargs):
        data_tracking = fetch_tracking_data(cod=self.post_code)
        if not data_tracking.get('status'):
            raise ValueError(data_tracking.get('data'))
        print('FOI!!', data_tracking.get('data'))

    def finalizate_ship(self, *args, **kwargs):
        ...

    def calculate_price_shipping(self, *args, **kwargs) -> float:
        url = 'https://www.melhorenvio.com.br/api/v2/me/shipment/calculate'
        melhor_envio_token = os.environ.get('MELHOR_ENVIO_TOKEN')
        headers = {
            "Accept": 'application/json',
            'Content-Type': 'applcation/json',
            'Authorization': f'Bearer {melhor_envio_token}',
            'User-Agent': 'Aplicação joaogood@outlook.com'
        }
        paylod = {
            "from": { 
                "postal_code": str(self._from)
            },  
            "to": {
                "postal_code": str(self._to)
            },
            "package": { # book params averange
                "height": 2,
                "width": 16,
                "length": 23,
                "weight": 0.5
            }
        }
        print('PAYLOD DO POST: ', paylod)
        try:
            request = requests.post(url=url, headers=headers, json=paylod)
            request.raise_for_status()
            response = request.json()
            return response[1]                                                                      

        except Exception as err:
                return f'Não foi possível calcular o frete: {err}'

