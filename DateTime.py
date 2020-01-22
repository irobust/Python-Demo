from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

today = date.today()
print("Today is ", today)

days = ['monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(today.weekday(), days[today.weekday()])

now = datetime.now()
print("Current datetime is ", now)

print(now.strftime("The current year is %Y"))
print(now.strftime("%a, %d %b %y"))

print(now.strftime("Current time is %I:%M:%S"))
print(now.strftime("Current time is %H:%M:%S"))

nextYear = now + timedelta(weeks=53)
print(str(nextYear))

nextWeek = now + timedelta(weeks=1, days=3)
print(str(nextWeek))

lastWeek = now - timedelta(weeks=1)
print(lastWeek.strftime("Last week is %a, %d %b %y"))

newYear = date(2021, 1, 1)
# newYear = newYear.replace(year=2020)
if(today > newYear):
    print('already went')
elif(today == newYear):
    print("Today is New Year's day")
else:
    print('Will comming')

timeToNewYear = newYear - today
print("It's just ", timeToNewYear.days, " days")

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2020, 1, 0, 0)
print(str)

html = calendar.HTMLCalendar(calendar.SUNDAY)
str = html.formatmonth(2017, 1)
print(str)

