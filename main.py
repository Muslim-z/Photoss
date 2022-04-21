import telegram
import os
from dotenv import dotenv_values
import time

TELEGRAM_TOKEN = dotenv_values('.env')['TELEGRAM_BOT_TOKEN']
TELEGRAM_CHANNEL_ID = dotenv_values('.env')['TELEGRAM_CHANNEL_ID']
DELAY = dotenv_values('.env')['DELAY']

if __name__ == "__main__":

    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    sap = os.walk('images')
    for root, dirs, files in os.walk('images'):
        for filename in files:
            image_path = f'{root}/{filename}'
            bot.send_document(chat_id=TELEGRAM_CHANNEL_ID,
                              document=open(image_path, 'rb'))
            time.sleep(int(DELAY))
