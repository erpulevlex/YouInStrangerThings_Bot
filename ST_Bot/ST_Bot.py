import telebot
from telebot import types
import random
bot=telebot.TeleBot('8548790337:AAGlX6QXbJrQuXqhxVekzwwT_8EIBUF21lc')

@bot.message_handler(commands=['start'])
def info(message):
        markup = types.InlineKeyboardMarkup()
        btn1=types.InlineKeyboardButton('Кто я из Очень странных дел?',callback_data='Yo1')
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton('Выживу я или нет?', callback_data='Нет')
        btn3 = types.InlineKeyboardButton('Мы победим Векну?', callback_data='Да')
        markup.row(btn2,btn3)
        bot.send_message(message.chat.id, 'Ну давай разбираться😎', reply_markup=markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data=='Да':
        bot.send_message(callback.message.chat.id, 'Конечно мы его победим!')
    elif callback.data == 'Yo1':
        images = ['./elev.webp','./maks.webp','./steve.webp','./dustin.webp','./eddie.webp','./hopper.webp','./mike.webp','./lukas.webp','./murray.webp','./will.webp']
        img = random.choice(images)
        file = open(img, 'rb')
        bot.send_photo(callback.message.chat.id, file)
        if img== './elev.webp':
            bot.send_message(callback.message.chat.id, 'Ты Оди! У тебя сверхспособности и двойка по математике')
        elif img=='./steve.webp':
            bot.send_message(callback.message.chat.id, 'Ты Стив! Мда, жаль этого добряка...')
        elif img=='./maks.webp':
            bot.send_message(callback.message.chat.id, 'Ты Макс! Надеемся что вылечишься, но вкус надо менять...')
        elif img=='./dustin.webp':
            bot.send_message(callback.message.chat.id, 'Ты Дастин! Ну красавчик, ни дать, ни взять')
        elif img=='./eddie.webp':
            bot.send_message(callback.message.chat.id, 'Ты Эдди! Земля пуховиком, брат панк')
        elif img=='./hopper.webp':
            bot.send_message(callback.message.chat.id, 'Ты Хоппер! Просто будь моим отцом, мужчина!')
        elif img=='./mike.webp':
            bot.send_message(callback.message.chat.id, 'Ты Майк! Я бы назвал тебя Изя')
        elif img=='./lukas.webp':
            bot.send_message(callback.message.chat.id, 'Ты Лукас! Тут и говорить нечего')
        elif img=='./will.webp':
            bot.send_message(callback.message.chat.id, 'Ты Уилл! Мутный ты тип, лучше не связываться')
        elif img=='./murray.webp':
            bot.send_message(callback.message.chat.id, 'Ты Мюррэй! Вот с кем, с кем, а с тобой бы я выпил')

    elif callback.data=='Нет':
        ans=['Конечно да!','Пока не понятно, будущее туманно','Не-а, тебя слопали']
        ansr=random.choice(ans)
        bot.send_message(callback.message.chat.id, ansr)
bot.polling(none_stop=True)