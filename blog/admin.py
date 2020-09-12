from django.contrib import admin
from .models import Post, PostStatisticAdmin, Email, EmailStatisticAdmin, Comment, CommentStatisticAdmin

# Register your models here.
admin.site.register(Post, PostStatisticAdmin)
admin.site.register(Email, EmailStatisticAdmin)
admin.site.register(Comment, CommentStatisticAdmin)
admin.site.site_header = 'Ahmad\'s Blog'
