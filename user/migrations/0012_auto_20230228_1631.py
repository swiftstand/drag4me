# Generated by Django 3.2.7 on 2023-02-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20230203_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragprofile',
            name='facebook',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dragprofile',
            name='instagram',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dragprofile',
            name='mail',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dragprofile',
            name='tiktok',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dragprofile',
            name='tip_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dragprofile',
            name='twitter',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dragprofile',
            name='youtube',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
