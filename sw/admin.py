from django.contrib import admin

# Register your models here.
from sw import models

admin.site.register(models.Message)
admin.site.register(models.Note)