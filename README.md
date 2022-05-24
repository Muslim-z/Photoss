# Photoss
Этот скрипт создан чтобы скачивать фотографии от NASA и SpaceX, и публиковать их в телеграм канал.

### Как установить
Для начала нужно создать файл `.env` в папке со скриптом и заполнить по шаблону:
```
NASA_API_KEY=ТУТ_ВАШ_API_KEY
TELEGRAM_BOT_TOKEN=ТУТ_ВАШ_ТОКЕН_ТЕЛЕГРАМ_БОТА
TELEGRAM_CHANNEL_ID=ТУТ_ПРИГЛАШЕНИЕ_В_ВАШ_ТЕЛЕГРАМ_КАНАЛ
DELAY=ТУТ_ЗАДЕРЖКА_МЕЖДУ_ОТПРАВКОЙ_ФОТОГРАФИЙ_В_СЕКУНДАХ
```

Чтобы получить NASA api key вам нажно зарегистрироваться на сайте [NASA](https://api.nasa.gov/).

Чтобы получить токен телеграм бота вам нужно его зарегистрировать у главного бота @BotFather.
Вот [инструкция](https://bit.ly/3Eg8c8f).

Затем бота нужно добавить в ваш телеграмм канал и назначить администратором.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить
Чтобы скачать фото от NASA нужно найти путь к файлу `nasa_photos.py` и написать в консоль:
```
python nasa_photos.py
```
Чтобы скачать фото от SpaceX нужно найти путь к файлу `spacex_photos.py` и написать в консоль:
```
python spacex_photos.py
```
Чтобы начать публикацию фото нужно найти путь к файлу `main.py` и написать в консоль:
```
python main.py
```

### Цель проекта
Хочу чтобы люди могли публиковать и просматривать красивые фото от NASA и SpaceX в свoём телеграм канале.
