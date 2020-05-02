# Generated by Django 3.0.5 on 2020-05-02 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0005_auto_20200425_2237'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_customeruser_is_garage_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('check_out_time', models.DateTimeField(null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Car')),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.Garage')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
