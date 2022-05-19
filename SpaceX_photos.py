import os
import requests

from tools import save_image
from tools import find_extention
from urllib.parse import urlparse

FILE_DIR = 'images/'


def fetch_spacex_last_launch():
    launches_url = 'https://api.spacexdata.com/v3/launches/66'
    response = requests.get(launches_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr_images']

    for number, image in enumerate(image_links):
        filepath = f'{FILE_DIR}last_launch_photo{number}{find_extention(image)}'
        save_image(image, filepath)


if __name__ == "__main__":
    fetch_spacex_last_launch()
