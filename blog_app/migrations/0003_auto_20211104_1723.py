# Generated by Django 3.2.7 on 2021-11-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20211026_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]
