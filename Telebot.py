import telebot
import time
import schedule
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('token_bot'))
id_chat = (os.getenv('id_chat_key'))

def morning_message():
    bot.send_message(id_chat, 'Всем доброе утро!')


schedule.every().wednesday.at("09:00").do(morning_message)
while True:
    schedule.run_pending()
    time.sleep(60)