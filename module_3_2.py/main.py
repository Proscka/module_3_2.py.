def  send_email(messag,recipient,*,sender="university.help@gmail.com"):
    if "@"not in sender or not sender.endswith ((".com", ".ru", ".net", ".COM", ".RU",".NET"))or\
            "@" not in recipient or not recipient.endswith((".com",".ru",".net",".COM",".RU",".NET")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return
    if sender==recipient:
        print("Невозможно отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса{sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

print(send_email("Это сообщение для проверки связи","vasyok1337@gmail.com"))
print(send_email("Вы видете это сообщение как лучший студент курса!","urban.fan@mail.ru",
sender="urban.info@gmail.com"))
print(send_email("Пажалуйста, исправте задание","urban.student@mail.ru",sender="urban.teacher@mail.uk"))
print(send_email("Напоминаю самому себе о вебинаре","urban.teacher@mail.ru",sender="urban.teacher@mail.ru"))


