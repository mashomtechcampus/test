# Generated by Django 2.2.3 on 2019-07-30 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
    ]
