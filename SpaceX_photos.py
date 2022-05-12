import os
import requests

from tools import save_image
from tools import find_extention
from urllib.parse import urlparse

SPACEX_FILENAME = f'images/last_launch_photo{number}{find_extention(image)}'

def fetch_spacex_last_launch():
    launches_url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(launches_url)
    response.raise_for_status()
    image_links = response.json()[66]['links']['flickr_images']

    for number, image in enumerate(image_links):

        save_image(image, SPACEX_FILENAME)

if __name__ == "__main__":
    fetch_spacex_last_launch()
