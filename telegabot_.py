import telebot
from telebot import types
# a = '1288453749:AAHy5OsaBLxKOphGl4ai_5fOgoIXnAtG1Ig'
bot = telebot.TeleBot('1298360192:AAGDl_7jT5cUmsWkuJhHmJiRVgQqryJ8NvU', parse_mode=None) 

keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard= True,row_width=2)
k1 = types.KeyboardButton('Hello')
k2 = types.KeyboardButton('bye')
k3 = types.KeyboardButton('sticker')
keyboard.add(k1, k2, k3)

inline_kb = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Погода', callback_data='1')
btn2 = types.InlineKeyboardButton ('News',callback_data='2')
inline_kb.add(btn1,btn2)

@bot.callback_query_handler(func=lambda call:True)
def calback_inline(call):
    chat_id = call.message.chat.id 
    mes_id = call.message.message_id
    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Pogoda nice',reply_markup=keyboard)
    if call.data == '2':
        bot.edit_message_text(chat_id =chat_id, message_id=mes_id, text = 'news NICE')

@bot.message_handler(commands=['start'])
def start_mes(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Hello my King',
    reply_markup = inline_kb)
    print(message.text)
@bot.message_handler(content_types = ['text'])
def send_text(message):

    main_kb = types.ReplyKeyboardMarkup(resize_keyboard= True)
    k1 =types.KeyboardButton('Dohod')
    k2 = types.KeyboardButton('rasshod')
    main_kb.add(k1,k2)
    print(message.text)
    chat_id = message.chat.id
    if message.text.lower() == 'hello':
        bot.send_message(chat_id,' i tebe Hello',
        reply_markup=main_kb)
    elif message.text == 'bye':
        bot.send_message(chat_id, ' i tebe poka')
    elif message.text.lower() == 'sticker':
        bot.send_sticker(chat_id,'CAACAgIAAxkBAAMqX3VZoxiT9UgIXEdQVpIsQPOqFI8AAv4AA1advQraBGEwLvnX_xsE')



@bot.message_handler(content_types = ['sticker'])
def sticker_id(message):
    chat_id = message.chat.id
    bot.send_sticker(chat_id,'CAACAgIAAxkBAAMqX3VZoxiT9UgIXEdQVpIsQPOqFI8AAv4AA1advQraBGEwLvnX_xsE' )

    print(message)







bot.polling()