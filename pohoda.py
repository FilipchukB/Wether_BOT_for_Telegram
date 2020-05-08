import telebot
import pyowm

owm = pyowm.OWM('6d4050ec69444e19183c61382e5f4bb7', language='ua')

bot = telebot.TeleBot("900658304:AAEcHibwAx2NsGUcAnZJFWtDznXLe0Hwb1M")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Де бажаєте дізнатися погоду?")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    stan_pohodu = w.get_detailed_status()
    temp = w.get_temperature('celsius')["temp"]
    observation_list = owm.weather_around_coords(-22.57, -43.12)
    answer = "В місті " + message.text + " зараз " + stan_pohodu + "\n"
    answer += "Зараз температура " + str(temp)
    bot.send_message(message.chat.id, answer)
    print(observation_list)


bot.polling(none_stop=True)
