# Generated by Django 2.2 on 2020-10-01 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0003_auto_20201001_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wall_message',
            name='attachment',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
