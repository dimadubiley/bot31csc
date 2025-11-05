# import time
# import requests
# import random
# import os
# from dotenv import load_dotenv
# from PIL import Image
#
# taros = []
# for i in range(22):
#     taros.append(f'./tarots/{i}.jpg')
#
# load_dotenv()
# # bot_token = os.getenv("TOKEN")
# # url = f"https://api.telegram.org/bot{bot_token}/"
# bot_key = '8483621839:AAE3rRpjmovokqfiHjlPCpOXju_xC3ANp9M'
#
# url = f"https://api.telegram.org/bot{bot_key}/"  # don't forget to change the token!
#
#
# def last_update(request):
#     response = requests.get(request + 'getUpdates')
#     response = response.json()
#     results = response['result']
#     total_updates = len(results) - 1
#     return results[total_updates]
#
#
# def get_chat_id(update):
#     return update['message']['chat']['id']
#
#
# def get_message_text(update):
#     return update['message'].get('text', '')
#
#
# def send_message(chat, text):
#     params = {'chat_id': chat, 'text': text}
#     return requests.post(url + 'sendMessage', data=params)
#
#
# def send_sticker(chat, image_path):
#     """Конвертирует JPG → WEBP и отправляет как стикер"""
#     webp_path = image_path.replace('.jpg', '.webp')
#
#     # если нет .webp — создаём временно
#     if not os.path.exists(webp_path):
#         img = Image.open(image_path).convert("RGBA")
#         img.save(webp_path, 'webp')
#
#     with open(webp_path, 'rb') as sticker:
#         data = {'chat_id': chat}
#         files = {'sticker': sticker}
#         return requests.post(url + 'sendSticker', data=data, files=files)
#
#
# # --- основная логика ---
#
# def main():
#     update_id = last_update(url)['update_id']
#     while True:
#         time.sleep(3)
#         update = last_update(url)
#         if update_id == update['update_id']:
#             text = get_message_text(update).lower()
#             chat_id = get_chat_id(update)
#
#             if text == 'tarot':
#                 image_path = random.choice(taros)
#                 send_sticker(chat_id, image_path)
#             elif text == 'dice':
#                 a, b = random.randint(1, 6), random.randint(1, 6)
#                 c = a + b
#                 send_sticker(chat_id, f' You get {a} and {b}\n'
#                                       f'Resout: {c}')
#             elif text == 'da':
#                 send_message(chat_id, 'Da')
#             elif text == 'number':
#                 send_message(chat_id, f'Random number {random.randint(-10, 10)}')
#
#             update_id += 1
#
#
# if __name__ == '__main__':
#     main()

import time

import requests
import random

bot_key = '8483621839:AAE3rRpjmovokqfiHjlPCpOXju_xC3ANp9M'

url = f"https://api.telegram.org/bot{bot_key}/"  # don't forget to change the token!


def last_update(request):
    response = requests.get(request + 'getUpdates')
    # TODO: Uncomment just for local testing
    # print(response)
    response = response.json()
    # print(response)
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    try:
        update_id = last_update(url)['update_id']
        while True:
            # pythonanywhere
            time.sleep(3)
            update = last_update(url)
            if update_id == update['update_id']:
                if get_message_text(update).lower() == 'hi' or get_message_text(
                        update).lower() == 'hello' or get_message_text(update).lower() == 'hey':
                    send_message(get_chat_id(update), 'Greetings! Type "Dice" to roll the dice!')
                elif get_message_text(update).lower() == 'csc31':
                    send_message(get_chat_id(update), 'Python')
                elif get_message_text(update).lower() == 'gin':
                    send_message(get_chat_id(update), 'Finish')
                    break
                elif get_message_text(update).lower() == 'python':
                    send_message(get_chat_id(update), 'version 3.10')
                elif get_message_text(update).lower() == 'dice':
                    _1 = random.randint(1, 6)
                    _2 = random.randint(1, 6)
                    send_message(get_chat_id(update),
                                 'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')
                else:
                    send_message(get_chat_id(update), 'Sorry, I don\'t understand you :(')
                update_id += 1
    except KeyboardInterrupt:
        print('\nБот зупинено')


# print(__name__)
if __name__ == '__main__':
    main()
# print(__name__)
# print('HELLO') #При подключении файла как бибилиотеки import bot, в другой .py файл проекта, этот код будет запускатся при включении того, другого файла
