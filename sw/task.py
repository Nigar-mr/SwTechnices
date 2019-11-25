from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import send_mail


def send_verification_email(name, occupation, phone, confidential, subject, messages, date, email):
    subject, from_email, to = f'{subject}', settings.EMAIL_HOST_USER, email
    text_content = 'Verificate Email'
    # html_content = f'From: {name}/n Contact:  {phone} olan shexsden {subject} basliqli {messages} gelmiwdi'
    print(date)
    # print(email)
    html_content = f"<p>From: {name}</p>" \
                   f"<p>Occupation: {occupation}</p>" \
                   f"<p>Contact Details: {phone}</p>" \
                   f"<p>Confidential: {confidential}</p>" \
                   f"<p>Subject: {subject}</p>" \
                   f"<p>Messages: {messages}</p>" \
                   f"<p>Date: {date}</p>" \
        # f"<p>Confidential: {confidential}</p>"

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['munisisazade@gmail.com'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
