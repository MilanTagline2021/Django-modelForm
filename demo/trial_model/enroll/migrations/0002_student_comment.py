# Generated by Django 3.2.6 on 2021-10-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='N/A', max_length=40),
        ),
    ]
