import os
import telebot
bot = telebot.Telebot("API Key Here")

@bot.message_handler(commands=["Start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I'm Bhashitha chat bot")
@bot.message_handler (commands=["how"])   
def send_message(message):
    bot.send_message(message, "turbothrills.neocities.org")
    bot.polling()
      