import os

from flask import Flask, request
from telebot import types

import telebot

TOKEN = '5224036555:AAFQjBM8TZedk34QeXf4DONVVd6i-c5dEiM'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(content_types = ['text'])
def eho(message):
  if message.text == "/ves":
    bot.send_message(message.chat.id, 'Как тебя зовут?')
   


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
    
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://timurcool.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
