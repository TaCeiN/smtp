import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# Логин/Пароль/Файл
gmail_user = '[EMAIL]'
gmail_app_password = '[EMAIL_PASSWORD]'
filename = '[ATTACH_FILE]'

# Получатели
sender_to = ['[SENDER1]','[SENDER2]']

# Письмо
for i in sender_to:
    # Основная часть и Заголовок
    msg = MIMEMultipart()
    msg['From'] = '[YOUR_SENDER_EMAIL]'
    msg['To'] = i
    msg['Subject'] = "[YOUR_TOPIC]"
    # Тело Письма
    body = """
    <p>Уважаемый !<br>
    [EMAIL_BODY].<br>
    </p>
    """

    # Подпись в письме
    signature = """
    <p>С уважением,<br>
    [SIGNATURE]
    </p>
    """

    # Прикрепление файла к письму
    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(part)
    # Приклепление Тела и Подписи
    msg.attach(MIMEText(body, 'html', 'utf-8'))
    msg.attach(MIMEText(signature, 'html', 'utf-8'))

    # Попытка отправить письмо с обработкой исключений
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(gmail_user, gmail_app_password)
            server.sendmail(gmail_user, i, msg.as_string())
        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)