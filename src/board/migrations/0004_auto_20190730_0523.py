# Generated by Django 2.2.3 on 2019-07-30 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_slide_advertising'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide_advertising',
            name='Slide_img',
            field=models.URLField(max_length=250),
        ),
    ]
