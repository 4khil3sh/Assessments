import time
from time import mktime
from datetime import datetime
a = datetime.now()
a = str(a)
print(a)
b = a.split()
c = b[0]
d = b[1]
datetimeobject = datetime.strptime(c,'%Y-%m-%d')
newformat = datetimeobject.strftime('%d-%m-%Y')
print(newformat)
timeobject = time.strptime(d, '%H:%M:%S.%f')
print(timeobject)