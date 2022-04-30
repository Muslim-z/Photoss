import os
import requests

from urllib.parse import urlparse


def save_image(url, image_path):
    response = requests.get(url)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)


def find_extention(url):
    url_parse = urlparse(url)
    split_text = os.path.splitext(url_parse.path)
    return split_text[1]


def fetch_spacex_last_launch():
    launches_url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(launches_url)
    response.raise_for_status()
    image_links = response.json()[66]['links']['flickr_images']

    for number, image in enumerate(image_links):
        filename = f'images/last_launch_photo{number}{find_extention(image)}'
        save_image(image, filename)

if __name__ == "__main__":

    fetch_spacex_last_launch()
