# Generated by Django 3.0.5 on 2020-05-03 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_car'),
        ('garage', '0006_remove_timetable_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Car'),
            preserve_default=False,
        ),
    ]
