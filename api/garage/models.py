from django.db import models
from django.db import models
from users.models import Car
from django.utils import timezone
from django.contrib.auth.models import User

class Garage(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    address_number = models.CharField(max_length=3)
    country_code = models.CharField(max_length=4)
    hourly_rate = models.IntegerField()
    register_date = models.DateTimeField(default=timezone.now)
    opening_time = models.CharField(max_length=5)
    closing_time = models.CharField(max_length=5)
    currency = models.CharField(max_length=3)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return self.name

class TimeTable(models.Model):
    check_in_time = models.DateTimeField(default=timezone.now)
    check_out_time = models.DateTimeField(null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)