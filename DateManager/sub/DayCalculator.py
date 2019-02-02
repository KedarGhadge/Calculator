from datetime import date
from datetime import time
from datetime import datetime
import DateManager.sub.DateAccepter
import DateManager.sub.Today

class Calculate(object):

    def CheckAge(self):
        try:
            oDateAccpter=DateManager.sub.DateAccepter.Accept()
            bDate=oDateAccpter.acceptDate("Please Enter B'date in format DD-mm-YYYY: ")
            now=DateManager.sub.Today.ToDate()
            oTodate,oToday=now.getToday()   #get today's date with Day
            birthDate=(oTodate-bDate).days # Subtract Today's date with entered date
            print(birthDate)
            #convert days into year,month and days
            years=int(int(birthDate)/365)
            weeks=int((int(birthDate)%365)/7)-1
            days=int(int(birthDate)%365%7)
            return str(years),str(weeks),str(days)
        except Exception as e:
            print (str(e))
