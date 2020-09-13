from django.contrib import admin
from .models import Post, PostStatisticAdmin, Email, EmailStatisticAdmin, Comment,\
    CommentStatisticAdmin, About, Announcements

# Register your models here.
admin.site.register(Post, PostStatisticAdmin)
admin.site.register(Email, EmailStatisticAdmin)
admin.site.register(Comment, CommentStatisticAdmin)
admin.site.register(About)
admin.site.register(Announcements)
admin.site.site_header = 'XMUM Student Council'
