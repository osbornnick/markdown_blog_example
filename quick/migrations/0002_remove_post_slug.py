# Generated by Django 2.2.5 on 2019-11-26 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quick', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
