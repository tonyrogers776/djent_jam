# Generated by Django 2.2 on 2020-10-01 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0002_auto_20200927_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='wall_message',
            name='attachment',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='instruments_played',
            field=models.CharField(max_length=255),
        ),
    ]