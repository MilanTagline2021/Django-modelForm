# Generated by Django 3.2.8 on 2021-10-08 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20211008_0912'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserData',
            new_name='User',
        ),
    ]
