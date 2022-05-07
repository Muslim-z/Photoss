import os
import time

import telegram

from dotenv import dotenv_values

if __name__ == "__main__":

    telegram_token = dotenv_values('.env')['TELEGRAM_BOT_TOKEN']
    telegram_channel_id = dotenv_values('.env')['TELEGRAM_CHANNEL_ID']
    delay = dotenv_values('.env')['DELAY']
    bot = telegram.Bot(token=telegram_token)
    for root, dirs, files in os.walk('images'):
        for filename in files:
            image_path = f'{root}/{filename}'
            with open(image_path, 'rb') as img:
                bot.send_photo(
                    chat_id=telegram_channel_id,
                    photo=img.read()
                )
            time.sleep(int(delay))
