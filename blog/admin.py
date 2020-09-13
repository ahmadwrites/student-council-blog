from django.contrib import admin
from .models import Post, PostStatisticAdmin, Email, EmailStatisticAdmin, Comment,\
    CommentStatisticAdmin, About, Announcement

# Register your models here.
admin.site.register(Post, PostStatisticAdmin)
admin.site.register(Email, EmailStatisticAdmin)
admin.site.register(Comment, CommentStatisticAdmin)
admin.site.register(About)
admin.site.register(Announcement)
admin.site.site_header = 'XMUM Student Council'
