# Generated by Django 2.2 on 2020-10-16 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0004_auto_20201001_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wall_message',
            name='attachment',
        ),
    ]
