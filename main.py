import telebot
bot = telebot.TeleBot('1747042451:AAH9wrLaBCKYdiT4kom1VGOXoLo0PawcHFg')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Привет {message.from_user.first_name}, как дела?')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    if message.text.lower() == 'как дела':
        bot.send_message(message.from_user.id, 'Хорошо!')
    if message.text == 'Хех:)':
        bot.send_message(message.from_user.id, '))')
    if message.text == 'Дискорд сервер бота':
        bot.send_message(message.from_user.id, 'https://forms.gle/Ltu3z5m4RnkcfpWH9')
    if message.text == 'Версия бота':
        bot.send_message(message.from_user.id, '0.1')
    if message.text == 'Пошел на хрен!' or message.text == 'Пошел на хер!' or message.text == 'Пошел на хуй!':
        bot.send_message(message.from_user.id, 'Тебя туда же!')
    if message.text == 'блять' or message.text == 'бля':
        bot.send_message(message.from_user.id, 'Ты ебобо?') 
    if message.text == 'Пошел на хрен!' or message.text == 'Пошел на хер!' or message.text == 'Пошел на хуй!':
        bot.send_message(message.from_user.id, 'Тебя туда же!')
    if message.text == 'Да':
        bot.send_message(message.from_user.id, 'Говна!')  
    else:
        bot.send_message(message.from_user.id, 'Шо? Я не понял')
bot.polling(none_stop=True)