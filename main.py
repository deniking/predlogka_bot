import telebot
from telebot import types

bot = telebot.TeleBot('5532731209:AAHgyl9pg5oRPIfku50F8r2XGqy6OJ479Fk')
chatID = '-1001689904782'


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(text='🔖 ПРЕДЛОЖИТЬ НОВОСТЬ', callback_data='btn1')
    item2 = types.InlineKeyboardButton(text='💰 ПРЕДЛОЖИТЬ РЕКЛАМУ', callback_data='btn2')
    markup.add(item1, item2)

    mess = f'ПРИВЕТ, <b>{message.from_user.first_name}!!!\n</b>при помощи этого <b>БОТА</b> ты можешь отправить нам в канал \n🇺🇦 ХАРЬКОВ ✌️ СМИ\n<u>новость</u> или <u>рекламу.</u>' \
           f'\n\n' \
           f'Нажми на соотвтствующую кнопку.'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)





@bot.callback_query_handler(func=lambda callback: callback.data)
def otvet(callback):
    if callback.data == 'btn1':
        markup_reply=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_now = types.KeyboardButton('ОТПРАВИТЬ НОВОСТЬ')
        markup_reply.add(item_now)
        bot.send_message(callback.message.chat.id, '📢Если у тебя есть новость, 📸 или 🎥 просто отправь её мне и я как можно скорее опубликую.', reply_markup=markup_reply)



    if callback.data == 'btn2':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_now = types.KeyboardButton('ОТПРАВИТЬ РЕКЛАМУ')
        markup_reply.add(item_now)
        bot.send_message(callback.message.chat.id, 'Для заказа рекламы напиши:\n- что рекламируешь (ссылку на канал тг или сайт)\n- если есть пример рекламного поста, отправь нам.', reply_markup=markup_reply)



@bot.message_handler(content_types=['text', 'photo', 'video', 'audio', 'voice'])
def checkbot_text(message):
    if message.text == message.text:
        bot.forward_message(chatID, message.chat.id, message.message_id)
        if message.text == 'ОТПРАВИТЬ НОВОСТЬ':
            bot.send_message(message.chat.id, 'Спасибо что делишься. Мы стараемся на благо Харькова и всех Харьковчан. \nЕсли хотите еще чтото отправить, перезапустите бота командой  /start')
        elif message.text == 'ОТПРАВИТЬ РЕКЛАМУ':
            bot.send_message(message.chat.id, 'Спасибо, детально о размещении и стоимости услуги, мы ответим в личное сообщение. ')


bot.polling(none_stop=True)
