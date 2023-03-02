# Generated by Django 3.2.7 on 2023-03-02 22:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_dragprofile_website_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followmanager',
            name='followers',
            field=models.ManyToManyField(related_name='user_followers', related_query_name='user_follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followmanager',
            name='following',
            field=models.ManyToManyField(related_name='followed_users', related_query_name='followed_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
