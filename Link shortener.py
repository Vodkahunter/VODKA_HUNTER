import requests
import telebot
from time import sleep
import os,sys
from time import sleep
import time
Z = '\x1b[1;31m'#احمر
X = '\x1b[1;32m'#اخضر
C = '\x1b[1;33m'#yellow
V = '\x1b[1;34m'#blue	
B = '\x1b[1;35m'#pink
N = '\x1b[1;36m'#لبني
M = '\x1b[1;37m'#ابيض	
def vodka(s):
 for ASU in s + '\n':
  sys.stdout.write(ASU)
  sys.stdout.flush()
  sleep(2./500)
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
vodka(N+current_time)  
vodka(X+'__     _____  ____  _  __    _    ')
vodka(Z+'\ \   / / _ \|  _ \| |/ /   / \   ')
vodka(X+' \ \ / / | | | | | |   /   / _ \  ')
vodka(Z+'  \ V /| |_| | |_| | . \  / ___ \ ')
vodka(X+'   \_/  \___/|____/|_|\_\/_/   \_\ ')
ID = "1318025489"
token = "1979815271:AAHVUDxi-FUR32VverNkuK21wE-QDjp4qNM"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])	
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text=f"*𝙷𝙸 𝚅𝙾𝙳𝙺𝙰 𝚂𝙴𝙽𝙳 𝚈𝙾𝚄𝚁  𝙻𝙸𝙽𝙺 𝚃𝙾 𝙱𝙴 𝚂𝙷𝙾𝚁𝚃𝙴𝙽\nBY @VoDkA_IQ | @VoDkA_PY*",parse_mode="markdown")
    bot.send_message(message.chat.id, text=f"*انت بس ابعت الرابط المطلوب و البوت هيختصرو \nBY @VoDkA_IQ*",parse_mode="markdown")
@bot.message_handler(func=lambda m: True)
def Get(message):
    try:
        msg = message.text
        bot.send_message(message.chat.id, text="Wait A minute")
        sleep(2)
        url = f'https://cvcbnhfuu.ml/HMD/api/ShortURL.php?url={msg}'
        sr = requests.get(url)
        res = sr.json()
        e = res['ShortURL']
        bot.send_message(message.chat.id,f"*𝙷𝙸 𝚅𝙾𝙳𝙺𝙰 𝙽𝙴𝚆 𝙻𝙸𝙽𝙺 𝚂𝙷𝙾𝚁𝚃𝙴𝙽:\n𝚈𝙾𝚄𝚁 𝙾𝚁𝙸𝙶𝙸𝙽𝙰𝙻 𝙻𝙸𝙽𝙺 : {msg}\n𝚈𝙾𝚄𝚁 𝚂𝙷𝙾𝚁𝚃𝙴𝙽 𝙻𝙸𝙽𝙺 : {e}\nBY @VoDkA_IQ | @VoDkA_PY*",parse_mode="markdown")

    except:
        pass
bot.polling(True)
