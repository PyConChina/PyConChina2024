# Generated by Django 5.1.1 on 2024-11-14 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='host',
            field=models.CharField(blank=True, help_text='Host of the room', max_length=32),
        ),
    ]
