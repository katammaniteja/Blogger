# Generated by Django 3.2.7 on 2021-11-30 14:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20211120_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
    ]
