# Generated by Django 4.0 on 2022-01-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination_new', '0003_remove_airport_a_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='a_image',
            field=models.ImageField(default='dragon_round.png', upload_to=''),
        ),
    ]
