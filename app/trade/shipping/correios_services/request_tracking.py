import requests

def fetch_tracking_data(cod: str) -> object:
    """ search in linketrack api with tracking-code, return object with data and status """
    cod = str(cod[0])
    url = f'https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo={cod}'
    print('URL DO VERIFY: ', url)
    print('cod: ', cod, type(cod))
    return request_data(url)


def request_data(url) -> object:
    headers = {
    'Accept': 'Application/json',
    }
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  
        data = response.json()
        return {
            'status': True,
            'data': data
        }
    
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as http_err:
        print('ERROR NO REQ: ', http_err)
        return {
            'status': False,
            'data': f'Erro ao consultar os correios, tente novamente!'
        }

