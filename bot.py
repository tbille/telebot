from telegram.ext import Updater, CommandHandler
import os
import requests

def totobot(bot, update):
    response = requests.get('http://smoke.toto.space', headers={"Content-Type": "application/json"})
    json = response.json()

    update.message.reply_text(
        'toto is winning even after {} days'.format(json["days"]))


token = os.getenv('TOKEN')
updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('toto', totobot))

updater.start_polling()
updater.idle()
