#import telepot
import telebot
import requests
import json
import urllib
import pyowm  

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
token = '1065167897:AAFqQSsIOsMlNbRvvgZyzsAPdVGXi6CPWYM'
api = 'a8bb95e658fdd84e0880066535b17743'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello! I`m @FlyB0T and i can help you to know current weather \n If you want to know more click /help')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Send me \'your city name\' and I show weather in YOUR city')

@bot.message_handler(content_types=['text'])
def weather(message):
    #need fix
    city = message.text
    api_address = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(city, api)
    json_data =requests.get(api_address).json()    
    if json_data['cod'] == 200:
        owm = pyowm.OWM(api)
        weather = owm.weather_at_place(city)
        w = weather.get_weather()
        temperature = w.get_temperature("celsius")["temp"]
        wind = w.get_wind()['speed']
        bot.send_message(message.chat.id, "Now in the " + str(city) +  
                     "\nTemperature - " + str(temperature) + ' \N{DEGREE SIGN}C\nSpeed - ' + str(wind) + ' m/s')
    else:
        bot.send_message(message.chat.id, 'Please enter again!')

if __name__ == "__main__":
    bot.polling(none_stop=True)