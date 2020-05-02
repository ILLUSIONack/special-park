from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone

class Car(models.Model):
    license_plate_number = models.CharField(max_length=12, primary_key=True)
    license_country_code = models.CharField(max_length=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)

    def getOwner(self):
        return self.owner

class CustomerUser(models.Model):
    iban = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    house_number = models.CharField(max_length=3)
    zip_code = models.CharField(max_length=4)
    is_garage_owner = models.BooleanField(default=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return 'Customer ' + self.user.username

class Transactions(models.Model):
    check_in_time = models.DateTimeField(null=False)
    check_out_time = models.DateTimeField(default=timezone.now)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    garage = models.ForeignKey('garage.Garage', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def calculateTimeInMin(self):
        pass

    def calculateCost(self):
        pass