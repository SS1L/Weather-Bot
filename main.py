import telepot
import telebot
import requests
import urllib, json  


token = '1065167897:AAFqQSsIOsMlNbRvvgZyzsAPdVGXi6CPWYM'
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
api = 'a8bb95e658fdd84e0880066535b17743'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello! I`m @FlyB0T and i can help you to know current weather \n If you want to know more click /help')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Send me \'your city\' and I find a weather')

@bot.message_handler(content_types=['text'])
def chip(message):
    '''
    first_city = message.text.split()[0]
    second_city = message.text.split()[1]
    a = next(item for item in data if item['name'] == first_city)
    b = next(item for item in data if item['name'] == second_city)
    if len(message.split()) == 3:
        bot.send_message(message.chat.id, 'Nice')
    else:
        bot.send_message(message.chat.id, 'Noob')
    '''    

bot.polling()