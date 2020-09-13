from django.contrib import admin
from .models import Password, PasswordStatisticAdmin
# Register your models here.
admin.site.register(Password, PasswordStatisticAdmin)
