# Generated by Django 3.2.7 on 2023-01-26 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_dragprofile_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragprofile',
            name='links',
            field=models.CharField(editable=False, max_length=1000, null=True),
        ),
    ]