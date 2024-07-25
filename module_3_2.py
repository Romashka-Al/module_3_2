def send_email(sms, recipient, *, sender='university.help@gmail.com'):
    if '@' not in (recipient or sender) or end(recipient) or end(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f'Нестандартный отправитель! Письмо отправлено с адреса {sender} на адрес {recipient}"')


def end(string):
    if string[-4:] == '.net' or string[-4:] == '.com' or string[-3:] == '.ru':
        return False
    return True


send_email("Нужно вовремя делать д/з", 'andrey2006@gmail.com')
send_email("Го в танки?", "3loyChel@yandex.ru", sender="bawunti@mail.ru")
send_email('ещкере', "botik@ti", sender="lol.gmail.com")
send_email('Чай поставьте', "family@mail.net", sender="family@mail.net")