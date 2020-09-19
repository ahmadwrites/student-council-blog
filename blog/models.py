from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from django.conf import settings
from django.core.mail import send_mail
from ckeditor.fields import RichTextField
from mywebsite.utils import unique_slug_generator
from django.contrib.auth.models import User

class Post(models.Model):
    TOPICS = (
        ('General', 'General'),
        ('Academics', 'Academics'),
        ('Sports', 'Sports'),
        ('Lifestyle', 'Lifestyle'),
        ('Events', 'Events'),
        ('Others', 'Others'),
    )

    title = models.CharField(blank=False, max_length=150)
    description = models.CharField(blank=False, max_length=100)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    content = RichTextField(blank=False)
    topic = models.CharField(max_length=20, choices=TOPICS, blank=False)
    image = models.ImageField(default='SOME STRING', upload_to='blog_image')
    views = models.IntegerField(editable=True, default=0)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Post)


class About(models.Model):
    title = models.CharField(blank=True, max_length=255)
    content = RichTextField()

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(blank=True, max_length=255)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.title


def send_mails(sender, instance, **kwargs):
    if kwargs['created']:
        message = f'Hello!\nWe have a new post: http://localhost:8000/post/{instance.id}\nEnjoy!\n\nKind regards'
        subject = 'New Blog Published!'
        to = Email.objects.values_list('email', flat=True).distinct()
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, to, fail_silently=True)


post_save.connect(send_mails, sender=Post)


class PostStatisticAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'views')
    search_fields = ('title',)


class Email(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class EmailStatisticAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    search_fields = ('email',)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    like_count = models.IntegerField(default='0')

    def __str__(self):
        return self.text[0:10]


class CommentStatisticAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'author')
    search_fields = ('post',)
