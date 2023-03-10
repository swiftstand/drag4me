# Generated by Django 3.2.7 on 2023-01-01 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ManyToManyField(related_name='user_followers', related_query_name='user_follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(related_name='followed_users', related_query_name='followed_user', to=settings.AUTH_USER_MODEL)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DragProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='user_default.png', upload_to='user_profile_pics')),
                ('about_me', models.TextField(blank=True, default='', null=True)),
                ('approval', models.BooleanField(default=False, editable=False)),
                ('locked', models.BooleanField(default=False, editable=False)),
                ('availability', models.TextField(default='Mondays', verbose_name='available_days_of_the_week')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
