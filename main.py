import telebot
from telebot import types

TOKEN = '2017397313:AAH7NFh4qZIqhlwBi3eR7LxLR0T73_Wk3dE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def constructor(massage):
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton(text='Heroku', url='https://www.heroku.com')
    buttonB = types.InlineKeyboardButton(text='GitHub', url='https://github.com')
    buttonC = types.InlineKeyboardButton(text='C')
    markup.add(buttonA)#, buttonB, buttonC
    bot.send_message(massage.chat.id, 'Ух ты! Работает', reply_markup=markup)


bot.infinity_polling()
