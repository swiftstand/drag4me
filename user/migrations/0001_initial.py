# Generated by Django 3.2.7 on 2023-01-01 12:09

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=100, unique=True, verbose_name='email')),
                ('username', models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=100000, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('fullname', models.CharField(default='swift only', max_length=100)),
                ('is_drag_performer', models.BooleanField(default=False)),
                ('city', models.TextField(default='input address')),
                ('agreement', models.BooleanField(default=True, verbose_name='Drag4me terms and condion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
