import requests
from django.conf import settings
from ..utils import translate_term


def fetch_volume_data(title:str, authors:list[str]) -> dict:
    """request book data from GoogleAPI with title and authors from client, then, return a object to merge data and save"""
    key = settings.GOOGLE_API_KEY
    print('key: ', key)
    title, authors = format_request_data(title=title, authors=authors)
    try:
        fetch_filds: list[str] = ['id', 'etag', 'volumeInfo'] #get only required necessary fields
        fetch_fields_format = ','.join(fetch_filds)

        url = f'https://www.googleapis.com/books/v1/volumes?q=intitle:{title}+inauthor:{authors}&fields=items({fetch_fields_format})&key={key}'
        response = requests.get(url)
        if response.status_code != requests.codes.ok:
            print('ERROR API GOOGLE: ', response.status_code, response.json())
            return {} 
        data = response.json()
        return get_format_book_data(data, title, authors)

    except Exception as error:  
        print('ERRO NO MERGE DOS DADOS: ', error)
        return {}

def format_request_data(title:str, authors:list[str])-> str:
    title_format = title.replace(' ', '+').strip()
    authors_format = ' '.join([author.strip() for author in authors])
    return title_format, authors_format

def get_format_book_data(data: object, title:str, authors:list[str]) -> object:
    if data:
        book_info = data['items'][0]
        volume_info = book_info['volumeInfo']
        return {
            'book_api_id': book_info.get('id'),
            'book_api_etag': book_info.get('etag'),
            'title': volume_info.get('title', title),
            'categories': volume_info.get('categories', []),
            'version': volume_info.get('contentVersion'),
            'language': volume_info.get('language', ''),  
            'authors': ', '.join(volume_info.get('authors', authors)),
            'description': volume_info.get('description', ''),
            'published_at': volume_info.get('publishedDate', ''),
            'total_pages': volume_info.get('pageCount', ''),
            'image': volume_info.get('imageLinks').get('thumbnail'),
        }  
    return {}    

if __name__ == '__main__':
    res = fetch_volume_data(title='O homem mais rico', authors=['george'])
    print(res)