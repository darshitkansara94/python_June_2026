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

# Print a date
day = currentdatetime.strftime('%d')
print(day)

month = currentdatetime.strftime('%B')
print(month)

month_num = currentdatetime.strftime('%b')
print(month_num)

time = currentdatetime.strftime('%H')
print(time)

second = currentdatetime.strftime('%M')
print(second)

# How to get a next value of date
increaseDay = currentdatetime + datetime.timedelta(days = 1)
print(increaseDay)

increaseYear = currentdatetime.replace(year = currentdatetime.year + 3)
print(increaseYear)

increaseMonth = currentdatetime.replace(month = currentdatetime.month + 3)
print(increaseMonth)

decreaseDay = currentdatetime - datetime.timedelta(days = 3)
print(decreaseDay)

decreaseYear = currentdatetime.replace(year = currentdatetime.year - 3)
print(decreaseYear)

decreaseMonth = currentdatetime.replace(month = currentdatetime.month - 3)
print(decreaseMonth)

increaseTime = currentdatetime + datetime.timedelta(hours = 2)
print(increaseTime)

increaseMinute = currentdatetime + datetime.timedelta(minutes = 2)
print(increaseMinute)

increasedateAndTime = currentdatetime + datetime.timedelta(days = 1,hours = 2)
print(increasedateAndTime)