# Generated by Django 5.1.1 on 2024-09-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='inventory',
            field=models.SmallIntegerField(),
        ),
    ]
