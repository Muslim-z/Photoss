import requests
import os
from urllib.parse import urlparse
def image_saver(url, image_path):
    response = requests.get(url)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)


def extention_print(url):
    url_parse = urlparse(url)
    split_text = os.path.splitext(url_parse.path)
    return split_text[1]

def fetch_spacex_last_launch():
    launches_url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(launches_url)
    response.raise_for_status()
    image_list = response.json()[66]['links']['flickr_images']

    for number, image in enumerate(image_list):
        filename = f'images/last_launch_photo{number}{extention_print(image)}'
        image_saver(image, filename)

fetch_spacex_last_launch()