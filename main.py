import os
import time

from pathlib import Path
from urllib.parse import urlparse

import telegram
import requests

from dotenv import dotenv_values


NASA_API_KEY = dotenv_values('.env')['NASA_API_KEY']
TELEGRAM_TOKEN = dotenv_values('.env')['TELEGRAM_TOKEN']


def extention_print(url):
    url_parse = urlparse(url)
    split_text = os.path.splitext(url_parse.path)
    return split_text[1]


def image_saver(url, image_path):
    response = requests.get(url)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    launches_url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(launches_url)
    response.raise_for_status()
    image_list = response.json()[66]['links']['flickr_images']

    for number, image in enumerate(image_list):
        filename = f'images/last_launch_photo{number}{extention_print(image)}'
        image_saver(image, filename)


def day_photo():
    apod_url = f'https://api.nasa.gov/planetary/apod?'\
        f'count=20&api_key={NASA_API_KEY}'
    response = requests.get(apod_url)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        filename = f'images/day_photo{number}{extention_print(image["url"])}'
        image_saver(image['url'], filename)


def EPIC_photo():
    epic_url = f'https://api.nasa.gov/EPIC/api/natural?api_key={NASA_API_KEY}'
    response = requests.get(epic_url)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        date = image['date'].replace("-", "/")
        epic_image_num = image['image']
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/'\
            f'{date.split()[0]}/png/{epic_image_num}.png?'\
            f'api_key={NASA_API_KEY}'
        filename = f'images/epic_photo{number}.png'
        image_saver(epic_image_url, filename)


# EPIC_photo()
# day_photo()
# fetch_spacex_last_launch()
if __name__ == '__main__':

    Path('images').mkdir(parents=True, exist_ok=True)
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    sap = os.walk('images')
    for root, dirs, files in os.walk('images'):
        for filename in files:
            image_path = f'{root}/{filename}'
            bot.send_document(chat_id='@rererereter',
                              document=open(image_path, 'rb'))
            time.sleep(86400)
