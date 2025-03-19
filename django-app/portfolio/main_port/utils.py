import requests
import json
from django.conf import settings

def send_telegram_message(chat_id: str, message: str):
    api_url = f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage'
    input_data = json.dumps({
        'chat_id': chat_id,
        'text': message,
        'parse_mode': "HTML"
    }).encode()
    try:
        response = requests.post(api_url, data=input_data, headers={'Content-Type': 'application/json'})
        return response.json()  # Возвращает ответ от Telegram
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
