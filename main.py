import telepot
import telebot
import requests
import urllib, json
import pyowm  


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

@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "In which city do you show the weather?")
    bot.register_next_step_handler(city, weath)

def weath(message):
    owm = pyowm.OWM("a8bb95e658fdd84e0880066535b17743")
    city = message.text
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    bot.send_message(message.chat.id, "Now in the " + str(city) +  
                     ", temperature - " + str(temperature)+ ' \N{DEGREE SIGN}C')


if __name__ == "__main__":
    bot.polling(none_stop=True)