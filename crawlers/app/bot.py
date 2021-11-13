from telegram.ext import Updater, CommandHandler
from telegram import parsemode
import os
from chat_request import get_request_result
import telebot
import html

#env variables defined in heroku
TOKEN = os.getenv("TOKEN")
PORT = int(os.getenv("PORT"))

#images
IMAGE_SNOO_WINKING = "https://i.ibb.co/Sfq91Fv/snoo.png"

Bot = telebot.TeleBot(TOKEN)

#Command handlers
def get_hot_subreddits(update, context):
    """send a message with all hot threads from subreddits requested"""
    results = get_request_result(context.args)
    for result in results:
         update.message.reply_text(text=result,parse_mode="HTML")   
         
def help(update, context):
    """send a message about how to use the bot"""

    texto ="""
    Envie:\n <code><b>/NadaPraFazer</b> SubReddit1; SubRed2...</code>
    Ou:\n <code><b>/npf</b> SubReddit1; SubReddit2...</code>
    \nVocê receberá só threads <b>BOMBÁSTICOS</b>
    Exemplo:\n /npf rocketLeague; AskScience""" + f"<a href='{IMAGE_SNOO_WINKING}'>.</a>"

    update.message.reply_text(text=texto,parse_mode="HTML")

def main():
    
    #Pass token to python-telegram-bot
    updater = Updater(TOKEN, use_context=True)

    #get user commands
    updater.dispatcher.add_handler(CommandHandler("npf", get_hot_subreddits))
    updater.dispatcher.add_handler(CommandHandler("nadaprafazer", get_hot_subreddits))
    updater.dispatcher.add_handler(CommandHandler("help", help))

    #webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,               
                          webhook_url = 'https://telegram-bot-challenge.herokuapp.com/' + TOKEN)
    #The pooling
    updater.idle()

if __name__ == '__main__':
    main()