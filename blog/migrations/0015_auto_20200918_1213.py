# Generated by Django 3.0 on 2020-09-18 04:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_auto_20200913_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_count',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
