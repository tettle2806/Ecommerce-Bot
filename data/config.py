import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admin_id = [
    1931305876
]

cashier = [
    627725876
]


type_of_review = ['😤Хочу пожаловатся 👎🏻',
                  '☹️Не понравилось, на 2 ⭐️⭐️',
                  '😐Удовлетворительно на 3 ⭐️⭐️⭐️',
                  '☺️Нормально, на 4 ⭐️⭐️⭐️⭐️',
                  '😊Все понравилось, на 5 ❤️']