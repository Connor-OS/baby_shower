import smtplib, ssl
from datetime import datetime


def send_reserve_email(gift, guest, message):
    port = 465
    password = "wsepqjfbfvdqpkll"

    sender_email = "arai.and.connor@gmail.com"
    receiver_email = ["coshaughnessy1@gmail.com", "akhmetovaarailym7@gmail.com"]
    email_template = """\
    Subject: Item {gift} bought by {guest}

    This is a test Email

    Hi there, the person {guest} has bought {gift} for you on {time}.
    
    message: {message}
    """.format(gift=gift, guest=guest, time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), message=message)

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("arai.and.connor@gmail.com", password)

        server.sendmail(sender_email, receiver_email, email_template)
