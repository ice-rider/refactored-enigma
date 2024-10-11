import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask_jwt_extended import get_jwt_identity


template_html = """
<html>
    <body>
        <h2>Добрый день, {username}!</h2>
        <p>Ваш код подтверждения: {code}</p>
    </body>
</html>
"""
template_plain = "Добрый день, {username}!\nВаш код подтверждения: {code}"

smtp_server = 'smtp.yandex.com'
smtp_port = 587
from_address = 'your_email@yandex.ru'  # Ваш адрес Яндекс.Почты
password = 'your_password'  # Ваш пароль от Яндекс.Почты


def send_email(email, name, code):
    # Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = email
    msg['Subject'] = 'Тема письма'

    # Добавление текста и HTML
    msg.attach(MIMEText(template_plain.format(username=name, code=code), 'plain'))
    msg.attach(MIMEText(template_html.format(username=name, code=code), 'html'))

    # Отправка письма
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Защита соединения
            server.login(from_address, password)
            server.send_message(msg)
            print('Письмо успешно отправлено!')
    except Exception as e:
        print(f'Ошибка при отправке письма: {e}')


def admin_access(func):
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        if user["role"] != "admin":
            return {"message": "Access denied"}, 403
        return func(*args, **kwargs)
    return wrapper


def user_verified(func):
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        if not user["verified"]:
            return {"message": "User not verified"}, 403
        return func(*args, **kwargs)
    return wrapper
