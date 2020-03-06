#!/bin/python

import requests
import random
from bot import bot_token, chat_id
from almost import almost
from now import now

almost = (random.choice(almost))
now = (random.choice(now))

print("Testing the bot")
print("Almost = ", almost)
print("Now = ", now)


def telegram_bot_sendtext(bot_message):
    bot_message = bot_message.replace("_", "\_")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)
    return response.json()


telegram_bot_sendtext(almost)

telegram_bot_sendtext(now)
