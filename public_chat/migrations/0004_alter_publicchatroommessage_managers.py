# Generated by Django 3.2.4 on 2021-06-07 20:25

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('public_chat', '0003_auto_20210607_0857'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='publicchatroommessage',
            managers=[
                ('room_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]