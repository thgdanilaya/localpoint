import email.message
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 465  # для SSL подключения
smtp_server = "smtp.yandex.ru"
sender_email = "llocalpoint@yandex.ru"  # Ваш емайл
receiver_email = "kazantsev.danilaya@yandex.ru"  # Емайл получателя
password = "jrjpblpsaifafkto"
code = 12345
# with open("template.html", encoding="utf8") as file:
#     text = file.read()

text = """
<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Код подтверждения</title>
    <link href='https://fonts.googleapis.com/css?family=Roboto:400,300,700,500' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="../fonts/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="../css/normalize.css">
    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdn.linearicons.com/free/1.0.0/icon-font.min.css">
    <link rel="stylesheet" href="../css/animate.min.css">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/magnific-popup.css">
    <style>
        body {
            background: rgb(248, 249, 250);
        }

        a {
            text-decoration: none;
        }
    </style>
</head>

<body>
    <script src="../js/bootstrap.bundle.js"></script>
    <script src="../js/wow.min.js"></script>
    <script src="../js/main.js"></script>
    <div class="modal modal-signin position-absolute d-block bottom-100 py-5" tabindex="-1" role="dialog"
        id="modalSignin">
        <center>
            <div class="row center my-5">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor"
                    class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
                    <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z" />
                </svg>
            </div>
        </center>

        <div class="modal-dialog my-0" role="document">
            <div class="modal-content rounded-4 ">
                <div class=" p-5  pb-4 border-bottom-0">
                    <h4 class="h4 mb-0">Здравствуйте, <span id="Name">Name</span>.</h4>
                </div>
                <div class=" px-5 pb-4 border-bottom-0">
                    <p class="fs-5">Ваш код авторизации:</p>
                </div>
                <div class="modal-body p-5 pt-0 px-5">
                    <div class=" rounded py-2 mb-2 bg-primary text-white">
                        <center class="p-0 m-0 display-6"><span style="letter-spacing: 0.4em" id="code">12345</span>
                        </center>
                    </div>

                </div>
            </div>
        </div>
    </div>
</body>

</html>

"""

message = MIMEText('html', text)
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Код подтверждения"
message.add_header('Content-Type', 'text/html')
message.set_payload("asolpdpaolsjmdpa")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
