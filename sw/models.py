from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    confidential = models.CharField(max_length=3)
    subject = models.CharField(max_length=255)
    messages = models.TextField()

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Note(models.Model):
    note = RichTextField()

