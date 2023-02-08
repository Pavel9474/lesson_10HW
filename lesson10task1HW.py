import telebot

bot = telebot.TeleBot("5897261595:AAGTJX0TOAAtWZVM13-QjpCcAdZZyb1LZBU")

# Задача 1. Напишите бота для техподдержки. 
# Бот должен записывать обращения пользователей в файл.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет я бот-помощник, какой у вас вопрос?")

@bot.message_handler(content_types=['text'])
def save_question(message):
    with open('messages.txt', 'a+', encoding='utf-8') as file:
        file.write(str(message.text)+'; '+ str(message.from_user.first_name)+str(message.from_user.last_name)+'; '+str(message.from_user.id)+'\n')
        bot.reply_to(message, "Ваше обращение зарегистрировано, оператор ответит вам в ближайшее время")
        bot.forward_message()
bot.infinity_polling()