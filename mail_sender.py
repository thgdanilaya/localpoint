import smtplib, ssl

port = 465  # для SSL подключения
smtp_server = "smtp.yandex.ru"
sender_email = "llocalpoint@yandex.ru"  # Ваш емайл
receiver_email = "voroshilovki@yandex.ru"  # Емайл получателя
password = "qyntutjzgqqlucuj"
message = "45145"
EMAIL_USE_TLS = True

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
