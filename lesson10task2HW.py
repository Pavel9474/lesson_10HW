import telebot
# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю.
bot = telebot.TeleBot("5897261595:AAGTJX0TOAAtWZVM13-QjpCcAdZZyb1LZBU")
def answer_question():
        with open('messages.txt', 'r', encoding='utf-8') as file:
            message_list=str(file.read()).split('\n')
            message_list_with_numbers=[]
            n=0
            for i in message_list:
                n=n+1
                message_list_with_numbers.append(str(n)+'; ' +i)
            print(message_list_with_numbers)
        number=int(input('Введите номер сообщения на которое хотите ответить: '))
        print (message_list_with_numbers[number-1])
        answer=input('Введите ответ: ')
        user_id=str(message_list_with_numbers[number-1]).split(';')
        user_id=user_id[3]
        print(user_id[1:])
        bot.send_message(str(user_id[1:]), str(answer))
answer_question()