import os
import requests
import datetime

from tools import save_image
from tools import find_extention
from urllib.parse import urlparse

from dotenv import dotenv_values

EPIC_FILENAME = f'images/epic_photo{number}.png'
NASA_FILENAME = f'images/day_photo{number}{find_extention(image["url"])}'
COUNT = 20

with open(image_path, 'wb') as file:
    file.write(response.content)


def fetch_epic_photo(nasa_api_key):
    epic_url = f'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': nasa_api_key}
    response = requests.get(epic_url,params=payload)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        date = image["date"]
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date = date.strftime("%Y/%m/%d")
        epic_image_num = image['image']
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/'\
            f'{date}/png/{epic_image_num}.png'
        save_image(epic_image_url, EPIC_FILENAME,params=payload)


def fetch_day_photo(nasa_api_key):
    apod_url = f'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_key,
        'count': COUNT
    }
    response = requests.get(apod_url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        save_image(image['url'], NASA_FILENAME)

if __name__ == "__main__":
    nasa_api_key = dotenv_values('.env')['NASA_API_KEY']
    fetch_day_photo(nasa_api_key)
    fetch_epic_photo(nasa_api_key)
