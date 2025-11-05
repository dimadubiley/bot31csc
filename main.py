import time
import requests
import random
import os
from dotenv import load_dotenv
from PIL import Image

taros = []
for i in range(22):
    taros.append(f'./tarots/{i}.jpg')

load_dotenv()
bot_token = os.getenv("TOKEN")
url = f"https://api.telegram.org/bot{bot_token}/"


def last_update(request):
    response = requests.get(request + 'getUpdates')
    response = response.json()
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    return update['message']['chat']['id']


def get_message_text(update):
    return update['message'].get('text', '')


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    return requests.post(url + 'sendMessage', data=params)


def send_sticker(chat, image_path):
    """Конвертирует JPG → WEBP и отправляет как стикер"""
    webp_path = image_path.replace('.jpg', '.webp')

    # если нет .webp — создаём временно
    if not os.path.exists(webp_path):
        img = Image.open(image_path).convert("RGBA")
        img.save(webp_path, 'webp')

    with open(webp_path, 'rb') as sticker:
        data = {'chat_id': chat}
        files = {'sticker': sticker}
        return requests.post(url + 'sendSticker', data=data, files=files)


# --- основная логика ---

def main():
    update_id = last_update(url)['update_id']
    while True:
        time.sleep(3)
        update = last_update(url)
        if update_id == update['update_id']:
            text = get_message_text(update).lower()
            chat_id = get_chat_id(update)

            if text == 'tarot':
                image_path = random.choice(taros)
                send_sticker(chat_id, image_path)
            elif text == 'dice':
                a, b = random.randint(1, 6), random.randint(1, 6)
                c = a + b
                send_sticker(chat_id, f' You get {a} and {b}\n'
                                      f'Resout: {c}')
            elif text == 'da':
                send_message(chat_id, 'Da')
            elif text == 'number':
                send_message(chat_id, f'Random number {random.randint(-10, 10)}')

            update_id += 1


if __name__ == '__main__':
    main()
