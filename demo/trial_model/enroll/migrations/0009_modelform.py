# Generated by Django 3.2.7 on 2021-10-07 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0008_auto_20211007_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelForm',
            fields=[
                ('manage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='enroll.manage')),
            ],
            options={
                'abstract': False,
            },
            bases=('enroll.manage',),
        ),
    ]