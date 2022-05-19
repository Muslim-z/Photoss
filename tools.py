import os

import requests

from urllib.parse import urlparse

def save_image(url, image_path,params=''):
    response = requests.get(url,params=params)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)

def find_extention(url):
    url_parse = urlparse(url)
    split_text = os.path.splitext(url_parse.path)
    return split_text[1]
