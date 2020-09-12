from django.contrib import admin
from .models import Post, PostStatisticAdmin, Email, EmailStatisticAdmin

# Register your models here.
admin.site.register(Post, PostStatisticAdmin)
admin.site.register(Email, EmailStatisticAdmin)
