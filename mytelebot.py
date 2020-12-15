import telebot
from telebot import types
import random

class GuessGame:
    random_number = 0
    number_of_tries = 0

TOKEN = '1255638994:AAG3mUlBd8lN1MsGsg6TOwvUAQUhdBnlSHU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    sti = open('./sticker.webp','rb')
    bot.send_sticker(message.chat.id, sti)
    chat_id = message.chat.id
    bot.send_message(chat_id,'Welcome my KIng or my Queen', reply_markup = inline_keyboard)
    
entry = {}
inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton('Ранг 1-100',callback_data = 'Ранг 1-100')
btn2 = types.InlineKeyboardButton('Ранг 1-1000',callback_data = 'Ранг 1-1000')
btn3 = types.InlineKeyboardButton('Ранг 1-10000',callback_data = 'Ранг 1-10000')
inline_keyboard.add(btn1,btn2,btn3)
@bot.callback_query_handler(func=lambda c:True)
def inline_(c):
    if c.data == 'Ранг 1-100':
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True,one_time_keyboard = True)
        btn1 = types.KeyboardButton('Начать игру')
        btn2 = types.KeyboardButton('Выход из игры')
        income_keyboard.add(btn1, btn2)
        msg = bot.send_message(c.message.chat.id, 'Что выбираете дальше?', reply_markup=income_keyboard)
        bot.register_next_step_handler(msg, get_category)
    if c.data == 'Ранг 1-1000':
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True,one_time_keyboard = True)
        btn1 = types.KeyboardButton('Начать игру')
        btn2 = types.KeyboardButton('Выход из игры')
        income_keyboard.add(btn1, btn2)
        msg = bot.send_message(c.message.chat.id, 'Что выбираете дальше?', reply_markup=income_keyboard)
        bot.register_next_step_handler(msg, get_category)
    if c.data == 'Ранг 1-10000':
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True,one_time_keyboard = True)
        btn1 = types.KeyboardButton('Начать игру')
        btn2 = types.KeyboardButton('Выход из игры')
        income_keyboard.add(btn1, btn2)
        msg = bot.send_message(c.message.chat.id, 'Что выбираете дальше?', reply_markup=income_keyboard)        
        bot.register_next_step_handler(msg, get_category)

    @bot.message_handler(commands=['ok'])
    def welcome(message, where_call=None):
        if where_call is None:
            global number
            number = random.randint(1, 100)
            msg = bot.send_message(message.chat.id, 'Хочешь выиграть приз? тогда закрой глаза, и загадай число и жди ответ!')
            attempt = 1
            bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))

        elif where_call == 'not_digit':
            msg = bot.send_message(message.chat.id, 'только числа')
            attempt = 1
            bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))

def random_number(message, attempt):
    if message.text.isdigit():
        n = int(message.text)
        if attempt < 7:
            attempt += 1
            if n < number:
                sti = open('./sticker2.webp','rb')
                bot.send_sticker(message.chat.id, sti)
                msg = bot.send_message(message.chat.id, 'Воу воу по легче, дай немного газу. Докинь сверу.')
                bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))
elif n > number:
                sti = open('./sticker3.webp','rb')
                bot.send_sticker(message.chat.id, sti)
                msg = bot.send_message(message.chat.id, 'Эу ты что? чуть по меньше давай. свои же)')
                bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))
            else:
                sti = open('./sticker4.webp','rb')
                bot.send_sticker(message.chat.id, sti)
                bot.send_message(message.chat.id, 'Поздравляем вас, с победой. Сегодня вы достойны аплодисментов!!!'.format(attempt - 1))
        else:
            sti = open ('./sticker7.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, 'А всё уже! Надо было раньше думать, давай ещё один круг, ты сможешь!\nзагаданное число {0}'.format(number))
    else:
        welcome(message, where_call='not_digit')




# @bot.message_handler(commands=['start'])
# def start_message(message):
#     sti = open('./sticker.webp','rb')
#     bot.send_sticker(message.chat.id, sti)
#     chat_id = message.chat.id
#     bot.send_message(chat_id,'Welcome my KIng or my Queen', reply_markup = inline_keyboard)

def get_category(message):
    chat_id = message.chat.id
    entry['category'] = message.text
    msg = bot.send_message(message.chat.id, 'ЧИСЛО? \nЕсть небольшой нюанс\nКликни меня /ok!\n И да начнётся БИТВА!')



bot.polling()