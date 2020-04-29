from .models import TimeTable

class TimeTableService:
    timeTable = None

    def __init__(self, license_plate, garage_id):
        self.timeTable = TimeTable.objects.get(car=license_plate,garage=garage_id)

    def getTimeTable(self):
        return self.timeTable

    def getCheckInTime(self):
        return self.timeTable.check_in_time