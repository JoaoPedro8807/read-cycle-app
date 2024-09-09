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

    def calculate_price_shipping(self, *args, **kwargs):
        url = 'https://www.melhorenvio.com.br/api/v2/me/shipment/calculate'
        headers = {
            "Accept": 'application/json',
            'Content-Type': 'applcation/json',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNjYyNDRhZDgxNmNjNDM4OGEwMzNkOGVhNmNjNWVlNDhiMDk3M2ZlMjRhZWNiMzhmODVjOGQxOWQ2NWNmMWY0NGFjNDY1NDZlOTNjMjE0NGIiLCJpYXQiOjE3MjQyODMxNzkuNDI4NjEzLCJuYmYiOjE3MjQyODMxNzkuNDI4NjE0LCJleHAiOjE3NTU4MTkxNzkuNDE1Mjk3LCJzdWIiOiI5Y2M1N2Y3Ni04ZDZjLTRlZmItYTBlNi1lMjY0Mzk1YTM4YWMiLCJzY29wZXMiOlsiY2FydC1yZWFkIiwiY2FydC13cml0ZSIsImNvbXBhbmllcy1yZWFkIiwiY29tcGFuaWVzLXdyaXRlIiwiY291cG9ucy1yZWFkIiwiY291cG9ucy13cml0ZSIsIm5vdGlmaWNhdGlvbnMtcmVhZCIsIm9yZGVycy1yZWFkIiwicHJvZHVjdHMtcmVhZCIsInByb2R1Y3RzLWRlc3Ryb3kiLCJwcm9kdWN0cy13cml0ZSIsInB1cmNoYXNlcy1yZWFkIiwic2hpcHBpbmctY2FsY3VsYXRlIiwic2hpcHBpbmctY2FuY2VsIiwic2hpcHBpbmctY2hlY2tvdXQiLCJzaGlwcGluZy1jb21wYW5pZXMiLCJzaGlwcGluZy1nZW5lcmF0ZSIsInNoaXBwaW5nLXByZXZpZXciLCJzaGlwcGluZy1wcmludCIsInNoaXBwaW5nLXNoYXJlIiwic2hpcHBpbmctdHJhY2tpbmciLCJlY29tbWVyY2Utc2hpcHBpbmciLCJ0cmFuc2FjdGlvbnMtcmVhZCIsInVzZXJzLXJlYWQiLCJ1c2Vycy13cml0ZSIsIndlYmhvb2tzLXJlYWQiLCJ3ZWJob29rcy13cml0ZSIsIndlYmhvb2tzLWRlbGV0ZSIsInRkZWFsZXItd2ViaG9vayJdfQ.dFWZRDFzSVFhqbtlB20OiMUzNed5tBgu0l3cI8cfo2oEgf3BqV72qX8JUG3bm3jnlW_Ns4sZ7iQp6-4B0_n5Gyg16KYnxFCApfa8_vl14VqXo6pLKwihcfDJPh4dGGdPupfMjJADyTi7uAYFBeewf0rDdzZLwToiBdQqoc-QTanr84mHAZu3eSAlyfYmtjlmDeWzK9dTyNTkCxq0_H5mOKxnIZijyb9vAtKbfhZMaS6zIoeiL0vq8TEEH__aVYn9uaxM7iAPRbEKFBD7wNMZAlkFQJOpWgnUCEW8Hh7Lrm3cR2Zy3VY3urR8DnMvNnZ26t_zSMswinHBiFI-UKPqFY0LLTg5vNlYtDGcCOxfDgknvZCS-pOamwF4JLzn5wyhAjWzi-veX4G768_3gwa7Wv3tzrlkxqLLmLGfMBk0N0NDSewUyrxfxvy2W15YjNKoaiLI345K6yWmvJjcXwszREt-le3t0osm_XTr8P8FDCv7qSrOJi6DYTkARl5qzCq7xzozyItwbMNeCX5CySWj4LC5F0i0arWD9T_WEfOH1vRKWibIj_Ineo0hnUmdya_CzpYZeAGqfOHi2m8SKH99SPZBTh1o04qOODvajD0s70RzcuSjWXXS7LEFpkQtADqVVnvpByBuV8jsQC3BIhKAiVUXayLTxUfXyI2ChMdi9Kc',
            'User-Agent': 'Aplicação joaogood@outlook.com'
        }
        paylod = {
            "from": { 
                "postal_code": self._from
            },
            "to": {
                "postal_code": self._to 
            },
            "package": { # book params averange
                "height": 2,
                "width": 16,
                "length": 23,
                "weight": 0.5
            }
        }
        try:
            request = requests.post(url=url, headers=headers, json=paylod)
            request.raise_for_status()
            response = request.json()
            return response[1]                                                                      

        except Exception as err:
                return f'Não foi possível calcular o frete: {err}'

