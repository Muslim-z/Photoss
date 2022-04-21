import requests
import  os
from dotenv import dotenv_values
from urllib.parse import urlparse

NASA_API_KEY = dotenv_values('.env')['NASA_API_KEY']


def extention_print(url):
    url_parse = urlparse(url)
    split_text = os.path.splitext(url_parse.path)
    return split_text[1]


def image_saver(url, image_path):
    response = requests.get(url)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)


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


def day_photo():
    apod_url = f'https://api.nasa.gov/planetary/apod?'\
        f'count=20&api_key={NASA_API_KEY}'
    response = requests.get(apod_url)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        filename = f'images/day_photo{number}{extention_print(image["url"])}'
        image_saver(image['url'], filename)

day_photo()
EPIC_photo()
