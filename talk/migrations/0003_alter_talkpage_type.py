# Generated by Django 5.1.1 on 2024-11-14 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0002_alter_author_options_remove_author_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkpage',
            name='type',
            field=models.CharField(choices=[('keynote', '主题'), ('lightning', '闪电'), ('roundtable', '圆桌')], default='keynote', max_length=32),
        ),
    ]
