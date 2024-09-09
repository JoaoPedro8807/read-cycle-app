import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code != requests.codes.ok:
            return None
            
        return ContentFile(response.content) 
    
    except Exception:
        return None