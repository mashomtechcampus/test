# Generated by Django 2.2.3 on 2019-11-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_cv_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
    ]
