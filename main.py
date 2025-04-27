# Рассматривая данный код, вы даёте согласие на то, что вы не будете редактировать его, а также, не будете продавать его.
# Также автор не несёт ни какой ответственности за использование данного кода. Все риски за использование данного софта лежат на вас.
# Last update: 16.04.2025 (19:29)

# Импорт необходимых ВСТРОЕННЫХ библиотек и модулей.

from banner import banner, ikon
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import json
import datetime

# Словарь для цветов.

COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
}

support_emails = ["aviver049@outlook.com", "ivarol788@gmail.com"]
# support_emails = ["sms@telegram.org", "dmca@telegram.org", "abuse@telegram.org", "sticker@telegram.org",
#                   "stopCA@telegram.org", "recover@telegram.org", "support@telegram.org", "security@telegram.org"]

# Вообще, в .venv есть необходимые модули. Не нужно их устанавливать. Но на всякий случай использую try/except.
# Попытка импорта необходимой сторонней библиотеки.

try:
    from pystyle import *
    import requests

# В случае отсутствия сторонней библиотеки, выводится инструкция по установке.

except ImportError:
    # Совет по установке модулей и выход
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка консоли.

    print(
        f'\n{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] {COLOR_CODE["GREEN"]}ВНИМАНИЕ У ВАС ПРОБЛЕМКА, НО МЫ ЕЁ РЕШИМ!{COLOR_CODE["RESET"]}')

    print(f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["GREEN"]}Оригинальное программное обеспечение находиться на: ' +
          f'{COLOR_CODE["CYAN"]}https://github.com/IjeDev1337/MadKillRedux{COLOR_CODE["RESET"]}\n' +
          f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["GREEN"]}' +
          f'Мы в телеграмме: {COLOR_CODE["CYAN"]}https://t.me/MadKillRedux{COLOR_CODE["RESET"]}')

    exit(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["GREEN"]}У вас отсутствует модули: ' +
         f'{COLOR_CODE["CYAN"]}pystyle и/или requests{COLOR_CODE["RESET"]}. {COLOR_CODE["RED"]}\n[*] {COLOR_CODE["GREEN"]}' +
         f'Напишите в терминал/консоль: {COLOR_CODE["RED"]}apt-get install python3-pip && pip3 install pystyle && pip3 install requests{COLOR_CODE["RESET"]}')


# Функция для отображения логотипа. (Только при старте кода)

def icon_logo():
    # Очистка консоли.
    os.system('cls' if os.name == 'nt' else 'clear')
    # Вывод приветственного экрана.
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, Center.XCenter(ikon))}")
    input(f"{Colorate.Horizontal(Colors.green_to_yellow, '')}")


# Функция для отображения основного экрана с меню и выбором действия.

def logo():
    # Очистка консоли.
    os.system('cls' if os.name == 'nt' else 'clear')
    # Вывод меню.
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, Center.XCenter(banner))}")
    print()


# Очень важная функция для отправки сообщения на электронную почту.

def send_message(to_email, subject,
                 message):  # to_email - адрес получателя, subject - тема сообщения, message - текст сообщения.
    # Чтение файла с данными отправителя.
    with open('senders.json') as f:
        data = json.load(f)
        from_email, password = next(iter(data.items()))

    # Дальше сложный код для отправки сообщения на почту. Понимать его необязательно, но если хотите, то можете посмотреть в интернете.

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    # Для почт @yandex.ru:

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()


# Функция для сноса аккаунта (выполняется при вводе 1).

def delete_account():
    # Очистка консоли.
    os.system('cls' if os.name == 'nt' else 'clear')
    # Вывод причин удаления аккаунта.
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '[+] Выберите причину удаления аккаунта:')}")
    print()  # Отступ.
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '1. Массовая рассылка сообщений.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '2. Распространение личных данных.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '3. Правокоционные действия, разжигание конфликта.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '4. Сексуальное влечение к несовершеннолетним.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '5. Ненастоящий номер, несоответствие информации.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '6. Использование Premium аккаунта для спама.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '7. Вернуться в главное меню.')}")
    print()  # Отступ.
    choice = input(f"{Colorate.Horizontal(Colors.green_to_yellow, "-> ")}")

    # Если выбрана первая причина удаления аккаунта, то выполняется код ниже.

    if choice == "1":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой спама. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно рассылает спам на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшего спама.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()


    elif choice == "2":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой распространения личных данных. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно распространяет личные данные на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшего распространения личных данных.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()


    elif choice == "3":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой провокационных действий и разжигания конфликта. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно провоцирует конфликты и разжигает негативные эмоции на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейших провокационных действий и разжигания конфликта.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()


    elif choice == "4":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой сексуального влечения к несовершеннолетним. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно проявляет сексуальное влечение к несовершеннолетним.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейших действий по отношению к несовершеннолетним.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()


    elif choice == "5":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой ненастоящего номера и маскировки личности. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно использует ненастоящий на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшего нарушения.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()


    elif choice == "6":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой использования Telegram-Premium для рассылки спама. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно использует подписку Premium для рассылки спама на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшего спама.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()


    elif choice == "7":
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(3)

        if __name__ == "__main__":
            main()

    else:
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Ошибка! Вы ввели неверный номер.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(3)

        if __name__ == "__main__":
            main()


def delete_channel():  # Функция для удаления канала.
    # Очистка консоли.
    os.system('cls' if os.name == 'nt' else 'clear')
    # Вывод причин удаления аккаунта.
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '[+] Выберите причину удаления канала:')}")
    print()  # Отступ.
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '1. Распространение личных данных.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '2. Жестокое обращение с животными.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '3. Порнография с несовершеннолетними.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '4. Канал с ценами на услуги доксинга и сватинга.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '5. Пропаганда наркотических средств.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '6. Вернуться в главное меню.')}")
    print()  # Отступ.
    choice = input(f"{Colorate.Horizontal(Colors.green_to_yellow, "-> ")}")

    if choice == "1":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой распространения личных данных. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно распространяет личные данные на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшего распространения личных данных.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()

    elif choice == "2":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой жестокого обращения с животными. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно жестоко обращается с животными на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшего жестокого обращения с животными.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()

    elif choice == "3":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой порнографии с несовершеннолетними. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно занимается порнографией с несовершеннолетними на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшей порнографии с несовершеннолетними.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()

    elif choice == "4":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой канала с ценами на услуги доксинга и сватинга. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно создает канал с ценами на услуги доксинга и сватинга на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшего создания канала с ценами на услуги доксинга и сватинга.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()

    elif choice == "5":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username нарушителя: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID нарушителя: ')}")
        violation_link = input(
            f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ссылку на нарушение в группе/канале: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой пропаганды наркотических средств. \n"
            f"\n"
            f"Я заметил, что пользователь с ID: {user_id} и именем пользователя {username} активно пропагандирует наркотические средства на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшей пропаганды наркотических средств.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()


    elif choice == "6":
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(3)

        if __name__ == "__main__":
            main()

    else:
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Ошибка! Вы ввели неверный номер.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(3)

        if __name__ == "__main__":
            main()


def delete_bot():  # Удаление бота из группы или канала.
    # Очистка консоли.
    os.system('cls' if os.name == 'nt' else 'clear')
    # Вывод причин удаления аккаунта.
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '[+] Выберите причину удаления бота:')}")
    print()  # Отступ.
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '1. Распространение личных данных.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '2. Нарко-магазин.')}")
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '3. Вернуться в главное меню.')}")
    print()  # Отступ.
    choice = input(f"{Colorate.Horizontal(Colors.green_to_yellow, "-> ")}")

    if choice == "1":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username бота: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID бота: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой распространения личных данных. \n"
            f"\n"
            f"Я заметил, что бот с ID: {user_id} и именем {username} активно продаёт личные данные на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшего нарушения.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()

    elif choice == "2":
        username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите @username бота: ')}")
        user_id = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ID бота: ')}")
        your_username = input(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Введите ваш @username: ')}")
        print()  # Отступ.

        subject = "Нарушитель на вашей платформе"  # Тема сообщения.
        message = (
            f"Здравствуйте, я являюсь пользователем вашего мессенджера и недавно столкнулся с проблемой продажи наркотиков. \n"
            f"\n"
            f"Я заметил, что бот с ID: {user_id} и именем {username} активно продаёт наркотики на вашем сервисе.\n"
            f"Я считаю, что это нарушает правила использования вашего сервиса и требует немедленного вмешательства.\n"
            f"Я прилагаю ссылку на нарушение: {violation_link}. Я прошу вас рассмотреть этот случай и принять соответствующие меры для предотвращения дальнейшего нарушения.\n"
            f"\n"
            f"Спасибо за вашу помощь. С уважением, {your_username}.")  # Текст сообщения.

        total_messages = int(
            input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество сообщений: ')}"))

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку сообщений...')}")
        time.sleep(3)

        # Цикл для отправки сообщений на почту. (Ожидание 0.5 секунд между каждым сообщением.)
        for email in support_emails:
            for i in range(total_messages):
                if i == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')

                send_message(email, subject, message)
                # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
                print(
                    f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
                time.sleep(0.5)

        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(5)

        # Возврат к основному меню.
        if __name__ == "__main__":
            main()


    elif choice == "3":
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(3)

        if __name__ == "__main__":
            main()


    else:
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Ошибка! Вы ввели неверный номер.')}")
        time.sleep(1)
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
        time.sleep(3)

        if __name__ == "__main__":
            main()



def send_user_message():  # Отправка сообщений пользователю.
    # Очистка консоли.
    os.system('cls' if os.name == 'nt' else 'clear')
    # Вывод причин удаления аккаунта.
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '[+] Введите требуемые данные:')}")
    print()  # Отступ.
    subject = input(f"{Colorate.Horizontal(Colors.green_to_yellow, '1. Введите тему сообщения: ')}")
    message = input(f"{Colorate.Horizontal(Colors.green_to_yellow, '2. Введите сообщение: ')}")

    print()  # Отступ.
    total_messages = int(input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество жалоб: ')}"))
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку жалоб...')}")

    for email in support_emails:
        for i in range(total_messages):
            if i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')

            send_message(email, subject, message)
            # Вывод сообщения об успешной отправке сообщения и количестве оставшихся сообщений.
            print(
                f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Сообщение номер {i + 1} отправлено успешно. Осталось отправить {total_messages - i - 1} сообщений.')}")
            time.sleep(0.5)

    print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка сообщений успешно завершена.')}")
    time.sleep(1)
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
    time.sleep(5)

    if __name__ == "__main__":
        main()


def delete_via_web():
    """
    Автоматически заполняет и отправляет форму на сайте Telegram support, используя библиотеку requests.
    Все параметры запрашиваются внутри функции.
    """

    url = "https://telegram.org/support"  # URL для отправки данных (нашли в инструментах разработчика)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, '[+] Введите информацию для заполнения формы.')}")
    print()  # Отступ.
    problem = input(f"{Colorate.Horizontal(Colors.green_to_yellow, '1. Опишите свою проблему: ')}")
    name = input(f"{Colorate.Horizontal(Colors.green_to_yellow, '2. Ваше полное имя, отчество и фамилия: ')}")
    email_address = input(f"{Colorate.Horizontal(Colors.green_to_yellow, '3. Введите ваш email: ')}")
    phone = input(f"{Colorate.Horizontal(Colors.green_to_yellow, '4. Номер телефона: ')}")
    print()  # Отступ.
    complaints = int(input(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Введите количество жалоб: ')}"))
    print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Начинаю отправку жалоб...')}")

    for i in range(complaints):
        if i == 0:
            os.system('cls' if os.name == 'nt' else 'clear')

        data = {
            "message": problem, # Используем правильные имена полей
            "legal_name": name,  # Используем правильные имена полей
            "email": email_address, # Используем правильные имена полей
            "phone": phone,  # Используем правильные имена полей
            "setln": "ru" # Добавляем поле setln (судя по данным формы)
        }

        try:
            response = requests.post(url, data=data)

            if response.status_code == 200:
                print(f"{Colorate.Horizontal(Colors.green_to_yellow, f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Жалоба номер {i + 1} отправлено успешно. Осталось отправить {complaints - i - 1} жалоб.')}")
                time.sleep(1)
            else:
                print(f"{Colorate.Horizontal(Colors.green_to_yellow, f"Ошибка при отправке жалобы {i + 1}. Status code: {response.status_code}")}")
                print(f"{Colorate.Horizontal(Colors.green_to_yellow, f"Текст ответа: {response.text}")}") # Добавлено для отладки

        except Exception as e:
            print(f"{Colorate.Horizontal(Colors.green_to_yellow, f"Произошла ошибка: {e}")}")


        if i == complaints - 1:
            print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Отправка жалоб успешно завершена.')}")
            time.sleep(1)
            print(f"{Colorate.Horizontal(Colors.green_to_yellow, 'Возвращаюсь в главное меню...')}")
            time.sleep(5)

            if __name__ == "__main__":
               main()  # Убедитесь, что функция main() определена


def main():  # Пока небольшой код для запуска основной функции.
    logo()
    choice = input(f"{Colorate.Horizontal(Colors.green_to_yellow, "[+] Ваш выбор > ")}")
    if choice == "1":  # Вызов функции удаления аккаунта.
        delete_account()

    elif choice == "2":  # Вызов функции удаления канала.
        delete_channel()

    elif choice == "3":  # Вызов функции удаления бота.
        delete_bot()

    elif choice == "4":  # Вызов функции отправки сообщений пользователю.
        send_user_message()


    elif choice == "5":  # Вызов функции отправки сообщений пользователю через сайт.
        delete_via_web()

    elif choice == "6":  # Управление почтами для отправки сообщений.
        pass

    elif choice == "7":  # Отправка сообщений пользователю через сайт.
        pass

    elif choice == "10":
        # os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colorate.Horizontal(Colors.green_to_yellow, '[!] Завершение работы...')}")
        time.sleep(3)
        exit()


# Запуск основной функции.
if __name__ == "__main__":
    icon_logo()
    main()
