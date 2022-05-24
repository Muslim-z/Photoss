import os
import requests

from datetime import datetime
from tools import save_image, find_extention
from urllib.parse import urlparse

from dotenv import dotenv_values

FILE_DIR = 'images/'
PHOTOS_COUNT = 20


def fetch_epic_photo(nasa_api_key):
    epic_url = f'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': nasa_api_key}
    response = requests.get(epic_url, params=payload)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        date = image["date"]
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date = date.strftime("%Y/%m/%d")
        epic_image_num = image['image']
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/'\
            f'{date}/png/{epic_image_num}.png'
        filepath = f'{FILE_DIR}epic_photo{number}.png'
        save_image(epic_image_url, filepath , params=payload)


def fetch_day_photo(nasa_api_key):
    apod_url = f'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_key,
        'count': PHOTOS_COUNT
    }
    response = requests.get(apod_url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        filepath = f'{FILE_DIR}day_photo{number}{find_extention(image["url"])}'
        save_image(image['url'], filepath)


if __name__ == "__main__":
    nasa_api_key = dotenv_values('.env')['NASA_API_KEY']
    fetch_day_photo(nasa_api_key)
    fetch_epic_photo(nasa_api_key)
