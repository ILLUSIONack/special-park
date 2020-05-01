from .models import TimeTable, Car
from django.db.models.base import ObjectDoesNotExist
from django.http import JsonResponse

class TimeTableService:
    timeTable = None

    def __init__(self, license_plate, garage_id):
        self.timeTable = TimeTable.objects.get(car=license_plate,garage=garage_id)

    def getTimeTable(self):
        return self.timeTable

    def getCheckInTime(self):
        return self.timeTable.check_in_time
    
    def deleteTime(self, user_id):
        # Transfer to Transactions table
        pass
        
        # Delete from table
        self.timeTable.delete()

class Visitor:
    time_table = None
    car = None
    status = { 'status': None, 'error': None, 'code': 200 }

    def __init__(self, license_plate):
        if not self.isValid(license_plate):
            return
            
        self.setTime(license_plate)
        self.setCar(license_plate)
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
            self.time_table = TimeTable.objects.get(car_id=license_plate)
        except ObjectDoesNotExist as err:
            print(f'Error message: {err}')
    
    def setCar(self, license_plate):
        try:
            self.car = Car.objects.get(license_plate_number=license_plate)
        except ObjectDoesNotExist as err:
            print(f'Error message: {err}')
    
    def setStatus(self):
        if self.time_table and self.car:
            # The visitor wants to go out
            self.status['status'] = True
            self.status['error'] = 'De bezoeker verlaat de garage.'
        elif not self.time_table and self.car:
            # The visitor wants to go in
            self.status['status'] = False
            self.status['error'] = 'De bezoeker betreedt de garage.'
        else:
            # The visitor does not exist
            self.status['status'] = None
            self.status['error'] = 'De bezoeker is geen klant.'
    
    def response(self):
        return JsonResponse({ 'status': self.status['status'], 'error': self.status['error'] }, status = self.status['code'])