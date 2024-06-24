# Generated by Django 4.2.13 on 2024-06-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneAssure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='preferred_time_zone',
            field=models.CharField(default='IST', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='dnd_end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='dnd_start_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
