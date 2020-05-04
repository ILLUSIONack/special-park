from users.models import Transactions
from .models import TimeTable, Car, Garage
from django.contrib.auth.models import User
from django.db.models.base import ObjectDoesNotExist
from django.http import JsonResponse
from django.utils import timezone

class Visitor:
    time_table = None
    car = None
    user = None
    status = { 'status': None, 'error': None, 'code': 200 }

    def __init__(self, license_plate):
        if not self.isValid(license_plate):
            return
            
        self.setCar(license_plate)
        self.setTime(license_plate)
        self.setStatus()
    
    def isValid(self, license_plate):
        if not license_plate:
            self.status['status'] = None
            self.status['error'] = 'Je hebt geen kenteken meegegeven!'
            self.status['code'] = 400
            return False
        if len(license_plate) != 8:
            self.status['status'] = None
            self.status['error'] = 'Dit is geen geldig kenteken!'
            self.status['code'] = 400
            return False
        return True
    
    def setTime(self, license_plate):
        try:
            self.time_table = TimeTable.objects.get(car_id=self.car)
        except ObjectDoesNotExist as err:
            print(f'Error message: {err}')
    
    def setCar(self, license_plate):
        try:
            self.car = Car.objects.get(license_plate_number=license_plate)
            self.user = self.car.getOwner()
        except ObjectDoesNotExist as err:
            print(f'Error message: {err}')
    
    def setStatus(self):
        if self.time_table and self.car:
            # The visitor wants to go out
            self.status['status'] = True
            self.status['error'] = 'De bezoeker verlaat de garage.'
            self.time_table.saveTime(self.time_table.getCheckIn(), self.car, self.user)
            self.time_table.delete()
        elif not self.time_table and self.car:
            # The visitor wants to go in
            self.status['status'] = False
            self.status['error'] = 'De bezoeker betreedt de garage.'
            new_visitor = TimeTable(car=self.car, garage=Garage.objects.get(id=1))
            new_visitor.save()
        else:
            # The visitor does not exist
            self.status['status'] = None
            self.status['error'] = 'De bezoeker is geen klant.'
    
    def response(self):
        return JsonResponse({ 'status': self.status['status'], 'error': self.status['error'] }, status = self.status['code'])