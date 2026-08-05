# Datetime :
#     Datetime is use to get time and date from the system.
#     This is not datatype or function.
#     We can fetch particular part from the date or from the time as well.
#     This object return date and time default system format.
#     To use / get datetime we need to import library 'datetime'.

import datetime

currentdatetime = datetime.datetime.now()
print(currentdatetime)

currentYear = currentdatetime.year
print(currentYear)

onlyyear = datetime.datetime.now().year
print(onlyyear)
