from telegram.ext import Updater, CommandHandler
import os
from chat_request import get_request_result
from flask import Flask

#env variables defined in heroku
TOKEN = os.getenv("TOKEN")

#images
IMAGE_SNOOSPIDER = "https://i.ibb.co/M9R6qg6/snoospider.png"

#Initializes the boot through /
app = Flask(__name__)
@app.route('/')
def hello():
    main()
    return 'Bot running...'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#Command handlers
def get_hot_subreddits(update, context):
    """send a message with all hot threads from subreddits requested"""
    results = get_request_result(context.args)
    for result in results:
         if not result:
             result = "você digitou algo errado ):"        
         update.message.reply_text(text=result,parse_mode="HTML")   
         
def help(update, context):
    """send a message about how to use the bot"""

    texto ="""
    Envie:\n <code><b>/NadaPraFazer</b> SubReddit1; SubRed2...</code>
    Ou:\n <code><b>/npf</b> SubReddit1; SubReddit2...</code>
    \nVocê receberá só threads <b>BOMBÁSTICOS</b>
    Exemplo:\n /npf rocketLeague; AskScience""" + f"<a href='{IMAGE_SNOOSPIDER}'>.</a>"

    update.message.reply_text(text=texto,parse_mode="HTML")

def main():
    
    #Pass token to python-telegram-bot
    updater = Updater(TOKEN, use_context=True)

    #get user commands
    updater.dispatcher.add_handler(CommandHandler("npf", get_hot_subreddits))
    updater.dispatcher.add_handler(CommandHandler("nadaprafazer", get_hot_subreddits))
    updater.dispatcher.add_handler(CommandHandler("help", help))

    #webhook
    #updater.start_webhook(listen="0.0.0.0",
    #                      port=int(PORT),
    #                      url_path=TOKEN,               
    #                      webhook_url = 'https://telegram-bot-challenge.herokuapp.com/' + TOKEN)
    
    #stay idle until receive a signal from telegram
    #updater.idle()

    updater.start_polling()

    