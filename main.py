import telebot
from telebot import types


with open('api.txt') as f:
    token = f.read()

bot = telebot.TeleBot(token.rstrip())


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Linux')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Python')
    btn3 = types.KeyboardButton('Сети')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    

def on_click(message):
    if message.text == 'Linux':
         bot.send_message(message.chat.id, 'https://www.youtube.com/playlist?list=PLmxB7JSpraiep6kr802UDqiAIU-76nGfc') 
    if message.text == 'Сети':
        bot.send_message(message.chat.id, 'https://habr.com/ru/articles/134892/')
    if message.text == 'Python':
        bot.send_message(message.chat.id, 'https://stepik.org/course/58852/syllabus?auth=login')


bot.polling(non_stop=True)
