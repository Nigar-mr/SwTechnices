from django import forms

from .models import Message


class MessagesForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'type': "text",
                'name': "name",
                'class': "form-control",
            }),
            'occupation': forms.TextInput(attrs={
                'type': "text",
                'name': "occupation",
                'class': "form-control",
            }),
            'phone': forms.TextInput(attrs={
                'type': "text",
                'name': "phone",
                'class': "form-control",
            }),
            'confidential': forms.TextInput(attrs={
                'type': "text",
                'name': "confidential",
                'class': "form-control",
            }),
            'subject': forms.TextInput(attrs={
                'type': "text",
                'name': "subject",
                'class': "form-control",
            }),
            'messages': forms.Textarea(attrs={
                'type': "text",
                'name': "messages",
                'class': "form-control",
                'rows': 4
            })
        }

        labels = {
            'name': 'From: ',
            'phone': 'Contact Details: ',
            'confidential': 'Confidential or not (Yes/No): ',
            'subject': 'Subject: ',
            'messages': 'Message: '
        }