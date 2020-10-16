# Generated by Django 2.2 on 2020-10-16 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0005_remove_wall_message_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=255)),
                ('gig_details', models.CharField(max_length=500)),
                ('contact_info', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='musician',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='instruments_played',
        ),
        migrations.DeleteModel(
            name='Band',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.AddField(
            model_name='gig',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_musician', to='jam.User'),
        ),
    ]