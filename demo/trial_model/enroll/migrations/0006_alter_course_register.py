# Generated by Django 3.2.7 on 2021-10-05 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_course_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='register',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='enroll.register'),
        ),
    ]
