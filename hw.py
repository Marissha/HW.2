def send_email(message, recipient, sender='university.help@gmail.com'):

    if sender.endswith('@', 0, len(sender)) == False and sender.endswith(('.com', '.ru', '.net'), 0, len(sender)) == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if recipient.endswith('@', 0, len(recipient)) == False and recipient.endswith(('.com', '.ru', '.net'), 0, len(recipient)) == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender in 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return

    if sender == recipient:
        print('Невозможно отправить письмо самому себе!')
        return

    if sender.endswith('university.help@gmail.com', 0, len(sender)) == False:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')