import os
import time

import telegram

from dotenv import dotenv_values

if __name__ == "__main__":

    TELEGRAM_TOKEN = dotenv_values('.env')['TELEGRAM_BOT_TOKEN']
    TELEGRAM_CHANNEL_ID = dotenv_values('.env')['TELEGRAM_CHANNEL_ID']
    DELAY = dotenv_values('.env')['DELAY']
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    for root, dirs, files in os.walk('images'):
        for filename in files:
            image_path = f'{root}/{filename}'
            with open(image_path, 'rb') as img:
                image = img.read()
            bot.send_photo(
                chat_id=TELEGRAM_CHANNEL_ID,
                photo=image
            )
            time.sleep(int(DELAY))
