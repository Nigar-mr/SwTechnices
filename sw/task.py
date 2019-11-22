from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import send_mail


def send_verification_email(name, occupation, phone, subject, messages, email):
    subject, from_email, to = f'{subject}', settings.EMAIL_HOST_USER, email
    text_content = 'Verificate Email'
    # html_content = f'From: {name}/n Contact:  {phone} olan shexsden {subject} basliqli {messages} gelmiwdi'
    print(name)
    print(email)
    html_content = f"<p>From: {name}</p>" \
                   f"<p>Occupation: {occupation}</p>" \
                   f"<p>Contact Details: {phone}</p>" \
                   f"<p>Subject: {subject}</p>" \
                   f"<p>Messages: {messages}</p>" \
                   f"<p>Email: {email}</p>" \
                   # f"<p>Confidential: {confidential}</p>"

    msg = EmailMultiAlternatives(subject, text_content, 'nigar-muradli@mail.ru', ['nigar-muradli@mail.ru'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
