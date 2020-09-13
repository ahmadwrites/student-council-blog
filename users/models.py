from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Password(models.Model):
    password = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now, editable=True)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.password


class PasswordStatisticAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username',)
