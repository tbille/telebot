import os
import requests
from telegram.ext import Updater, CommandHandler, PicklePersistence

def totobot(bot, update):
    response = requests.get('http://smoke.toto.space', headers={"Content-Type": "application/json"})
    json = response.json()

    update.message.reply_text(
        'toto is winning even after {} days'.format(json["days"]))

my_persistence = PicklePersistence(filename='my_file')

token = os.getenv('TOKEN')
updater = Updater(token, persistence=my_persistence, use_context=True)

updater.dispatcher.add_handler(CommandHandler('toto', totobot))

updater.start_polling()
updater.idle()
