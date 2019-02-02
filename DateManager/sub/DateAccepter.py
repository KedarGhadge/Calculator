from datetime import date
from datetime import time
from datetime import datetime
class Accept():
    def acceptDate(self,str1):
        try:
            date_entry = input(str1)
            day, month, year = map(int, date_entry.split('-'))
            date1 = date(year, month, day)
            return date1
        except Exception as e:
            print(str(e))
