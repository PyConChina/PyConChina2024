# Generated by Django 5.1.1 on 2024-10-08 09:55

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupporterPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('paragraph', 0), ('supporters', 8)], block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {'required': False}), 1: ('wagtail.blocks.CharBlock', (), {'required': True}), 2: ('wagtail.blocks.CharBlock', (), {'required': False}), 3: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 4: ('wagtail.blocks.URLBlock', (), {'required': False}), 5: ('wagtail.blocks.StructBlock', [[('name', 1), ('description', 2), ('logo', 3), ('url', 4)]], {}), 6: ('wagtail.blocks.ListBlock', (5,), {}), 7: ('wagtail.blocks.StructBlock', [[('heading', 1), ('supporters', 6)]], {}), 8: ('wagtail.blocks.ListBlock', (7,), {})}, help_text='Add supporters to the page.')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
