# Generated by Django 4.0 on 2021-12-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('roll_no', models.IntegerField()),
                ('college', models.CharField(max_length=40)),
                ('faculty', models.CharField(max_length=5)),
            ],
        ),
    ]
