from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from sw.models import Message
from sw.task import send_verification_email
from threading import Thread
User = get_user_model()

@receiver(post_save, sender=Message, dispatch_uid='send_mail_to_user')
def send_mail_to_user(*args, **kwargs):
    # print('I am working')
    obj = kwargs.get("instance")
    created = kwargs.get("created")
    if created:
        name = f"{obj.name}"
        occupation = f"{obj.occupation}"
        contact = f"{obj.phone}"
        confidential = f"{obj.confidential}"
        subject = f"{obj.subject}"
        messages = f"{obj.messages}"
        background_job = Thread(target=send_verification_email, args=(name, occupation, contact, confidential, subject, messages))
        print('Post is created')
        background_job.start()