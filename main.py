#!/bin/python

import requests
import random
from bot import bot_token, chat_id
from bijna import bijna
from nu import nu

print("Testing the bot")

bijna = (random.choice(bijna))
nu = (random.choice(nu))

def telegram_bot_sendtext(bot_message):
    bot_message = bot_message.replace("_", "\_")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)
    return response.json()


telegram_bot_sendtext(bijna)

telegram_bot_sendtext(nu)
