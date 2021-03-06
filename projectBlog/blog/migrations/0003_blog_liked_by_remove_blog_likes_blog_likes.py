# Generated by Django 4.0 on 2022-01-03 10:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_remove_blog_likes_blog_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
