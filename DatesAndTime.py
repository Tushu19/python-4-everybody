import datetime as dt
import time as tm

print(tm.time())

dtnow = dt.datetime.fromtimestamp(tm.time())
print('Current date and exact time:', dtnow)

print('Current date and time:',dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)

delta = dt.timedelta(days = 100)
print(delta)
today = dt.date.today() ## gets the exact date as of running the codes
print('Date today in format:', today)
print(today-delta)
print('Current time:', dtnow.hour, dtnow.minute, dtnow.second)
print('Current date', dtnow.year, dtnow.month, dtnow.day)
