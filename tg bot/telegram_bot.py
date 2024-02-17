import sqlite3
import telebot
from telebot import types

def create_connection():
    conn = sqlite3.connect('photos.db')
    return conn

bot = telebot.TeleBot('6480071971:AAGNeQb04u10ZZkk_gMNygB8vbFgunyhiC0')

def send_order_return_keyboard(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    order_button = types.InlineKeyboardButton("Оформити замовлення", callback_data="order")
    return_button = types.InlineKeyboardButton("Повернутись до вибору кольору", callback_data="return")
    keyboard.add(order_button, return_button)
    bot.send_message(chat_id, "Виберіть дію:", reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,'Французький бренд розпродує останні сумки минулого сезону підпільно так як вони не можуть продавати в відкриту, так дешево')
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    yellow_button = types.InlineKeyboardButton(text="Жовтий", callback_data="2")
    pink_button = types.InlineKeyboardButton(text="Рожевий", callback_data="1")
    red_button = types.InlineKeyboardButton(text="Червоний", callback_data="3")
    keyboard.add(yellow_button, pink_button, red_button)

    bot.send_message(message.chat.id, '👜Виберіть колір сумки:👜', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    try:
        if call.data == '1':
            bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('/photos/1.jpg', 'rb')), telebot.types.InputMediaPhoto(open(
                '/photos/6.jpg', 'rb'))])
            send_order_return_keyboard(call.message.chat.id)
        elif call.data == '2':
            bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('/photos/3.jpg', 'rb')), telebot.types.InputMediaPhoto(open(
                '/photos/2.jpg', 'rb'))])
            send_order_return_keyboard(call.message.chat.id)
        elif call.data == '3':
            bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('/photos/4.jpg', 'rb')), telebot.types.InputMediaPhoto(open(
                '/photos/5.jpg', 'rb'))])
            send_order_return_keyboard(call.message.chat.id)
        elif call.data == 'order':
            keyboard = types.InlineKeyboardMarkup()
            payment_button = types.InlineKeyboardButton(text="Перейдіть до оплати за посиланням: ", url="https://payeer.com/ru/account/add/?curr=USD")
            keyboard.add(payment_button)
            bot.send_message(call.message.chat.id, "💳Номер гаманця для оплати - P1111579533💳\n🛍Перейдіть до оплати за посиланням:🛍 ", reply_markup=keyboard)
        elif call.data == 'return':
            keyboard = types.InlineKeyboardMarkup(row_width=3)
            yellow_button = types.InlineKeyboardButton(text="Жовтий", callback_data="2")
            pink_button = types.InlineKeyboardButton(text="Рожевий", callback_data="1")
            red_button = types.InlineKeyboardButton(text="Червоний", callback_data="3")
            keyboard.add(yellow_button, pink_button, red_button)
            bot.send_message(call.message.chat.id, '👜Виберіть колір сумки:👜', reply_markup=keyboard)
        else:
            bot.send_message(call.message.chat.id, "Невірний ідентифікатор фото.")
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Помилка: {str(e)}")

bot.polling(none_stop=True)
