# Generated by Django 3.0.5 on 2020-05-03 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0006_remove_timetable_car'),
        ('users', '0008_customeruser_is_garage_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
    ]