from time import sleep
import os
import time
import telebot
import requests

bot = telebot.TeleBot('token')

# Freepik API URL
url = "https://www.freepik.com/api/icons"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Please enter a query to search for icons.")


@bot.message_handler(func=lambda message: True)
def handle_query(message):
    term = message.text
    params = {'format[search]': "1", 'locale': "en",
              'term': term, 'type[icon]': "1"}
    response = requests.get(url, params=params).json()

    if 'items' in response:
        items = response['items']
        for icon in items:
            icon_url = icon['thumbnails']['small']['url']
            bot.send_photo(message.chat.id, icon_url)
    else:
        bot.reply_to(message, "No icons found for your query.")


try:
    from cfonts import render, say
except:
    os.system("pip install python-cfonts")
    os.system("pip install render")


Z = "\033[1;31m"
F = "\033[2;32m"
B = "\033[2;36m"
X = "\033[1;33m"
C = "\033[2;35m"


def SAJ(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)


output = render("FREEPIK-BOT", colors=["white", "red"], align="center")
print(output)
SAJ(
    F
    + f"\033[1;32m\n                  『ᴍᴀᴅᴇ ʙʏ : ENG.DEV SAJJAD ™ \n                         ᴛᴇʟᴇɢʀᴀᴍ: https://t.me/S_J_O_D \n                            ᴄʜᴀɴɴᴇʟ : https://t.me/KING_OF_ENG  』",
    0.00,
    True,
)


bot.polling(non_stop=True, none_stop=True)
