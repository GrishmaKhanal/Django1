# Generated by Django 4.0 on 2021-12-28 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
    ]
