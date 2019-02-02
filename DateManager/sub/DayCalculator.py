from datetime import date
from datetime import time
from datetime import datetime
import DateManager.sub.DateAccepter
class Calculate(object):

    def CheckAge(self):
        try:
            oDateAccpter=DateManager.sub.DateAccepter.Accept()
            bDate=oDateAccpter.acceptDate("Please Enter B'date in format DD-mm-YYYY: ")
            return bDate
        except Exception as e:
            print (str(e))
