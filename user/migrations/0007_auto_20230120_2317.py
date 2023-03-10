# Generated by Django 3.2.7 on 2023-01-20 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20230120_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='dragprofile',
            name='facebook',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dragprofile',
            name='instagram',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dragprofile',
            name='mail',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dragprofile',
            name='tiktok',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dragprofile',
            name='twitter',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dragprofile',
            name='website_url',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dragprofile',
            name='youtube',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dragprofile',
            name='tip_url',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
