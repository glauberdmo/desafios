import telebot
from chat_request import get_request_result

CHAVE_API = "2122853882:AAFpucYaaJhzXSXw0O3gU44lE9rqs_M6csY"
IMAGE_SNOO_WINKING = "https://i.ibb.co/Sfq91Fv/snoo.png"

Bot = telebot.TeleBot(CHAVE_API)

@Bot.message_handler(commands=["npf"])
@Bot.message_handler(commands=["NadaPraFazer"])
def get_hot_threads(mensagem):
    results = get_request_result(mensagem.text)
    for result in results:
        Bot.send_message(mensagem.chat.id, result,parse_mode='HTML')

@Bot.message_handler(commands=["help"])
def responder(mensagem):
    texto ="""
    Envie:\n <code><b>/NadaPraFazer</b> SubReddit1; SubRed2...</code>
    Ou:\n <code><b>/npf</b> SubReddit1; SubReddit2...</code>
    \nVocê receberá só threads <b>BOMBÁSTICOS</b>
    Exemplo:\n /npf rocketLeague; AskScience""" + f"<a href='{IMAGE_SNOO_WINKING}'>.</a>"

    Bot.reply_to(mensagem, texto,parse_mode='HTML')

Bot.polling()