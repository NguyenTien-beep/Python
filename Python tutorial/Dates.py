import datetime as dt

x=dt.datetime.now()
print(x)

print(x.year)
print(x.strftime('%A')) # display the name of the weekday

x=dt.datetime(2929,4,15)
print(x)

print(x.strftime('%d'))  # display the name of the month
