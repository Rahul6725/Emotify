# Generated by Django 3.1.2 on 2020-10-22 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20201022_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='captured_images',
            name='user_name',
        ),
    ]
