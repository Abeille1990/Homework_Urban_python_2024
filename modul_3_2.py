ending = '.com', '.ru', '.net'
def send_email(message, recipient, sender = "university.help@gmail.com"):
    if '@' in recipient == True and '@' in sender == True:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес  {recipient}")
    elif recipient.endswith(ending) != True or sender.endswith(ending) != True:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес  {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на почту {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи','vasoyk1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса','urban.fan@mail.ru',"urban.info@gmail.com")
send_email('Пожалуйста, исправьте задание','urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре','urban.teacher@mail.ru','urban.teacher@mail.ru')