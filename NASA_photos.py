import os
import requests

from urllib.parse import urlparse

from dotenv import dotenv_values


def find_extention(url):
    url_parse = urlparse(url)
    root, extention = os.path.splitext(url_parse.path)
    return extention


def save_image(url, image_path,params=''):
    response = requests.get(url,params=params)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)


def fetch_epic_photo(nasa_api_key):
    epic_url = f'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': nasa_api_key}
    response = requests.get(epic_url,params=payload)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        date = image['date'].replace("-", "/")
        epic_image_num = image['image']
        epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/'\
            f'{date.split()[0]}/png/{epic_image_num}.png'
        filename = f'images/epic_photo{number}.png'
        save_image(epic_image_url, filename,params=payload)


def fetch_day_photo(nasa_api_key):
    apod_url = f'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_key,
        'count': 20
    }
    response = requests.get(apod_url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        filename = f'images/day_photo{number}{find_extention(image["url"])}'
        save_image(image['url'], filename)

if __name__ == "__main__":
    nasa_api_key = dotenv_values('.env')['NASA_API_KEY']
    fetch_day_photo(nasa_api_key)
    fetch_epic_photo(nasa_api_key)
