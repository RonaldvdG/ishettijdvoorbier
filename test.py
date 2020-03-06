#!/bin/python

import requests
from bot import bot_token, chat_id

text = input('Enter the text to be send: ')

print("Testing the bot")

def telegram_bot_sendtext(bot_message):
    bot_message = bot_message.replace("_", "\_")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)
    return response.json()

telegram_bot_sendtext(text)
