# Generated by Django 3.2.8 on 2021-10-08 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_rename_userdata_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
    ]
