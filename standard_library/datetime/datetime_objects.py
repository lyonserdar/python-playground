"""
datetime_objects.py
"""
import datetime

# Creates date object for the given dates
d1 = datetime.date(2021, 1, 1)
d2 = datetime.date(2021, 7, 31)
d3 = datetime.date(1990, 5, 7)

print(type(d1))
print(d1)
print(d2)
print(d3)
print()

# Creates time objects for the given times
t1 = datetime.time(12, 0, 0)
t2 = datetime.time(6, 30, 0)
t3 = datetime.time(9, 15, 0)

print(type(t1))
print(t1)
print(t2)
print(t3)
print()

# Creates datetime objects of the given dates
dt1 = datetime.datetime(2020, 7, 20, 11, 30, 0)
dt2 = datetime.datetime(1990, 3, 10, 12, 0, 0)
dt3 = datetime.datetime(2021, 1, 1, 0, 0, 0)

print(type(dt1))
print(dt1)
print(dt2)
print(dt3)
print()

# OUTPUT
# <class 'datetime.date'>
# 2021-01-01
# 2021-07-31
# 1990-05-07

# <class 'datetime.time'>
# 12:00:00
# 06:30:00
# 09:15:00

# <class 'datetime.datetime'>
# 2020-07-20 11:30:00
# 1990-03-10 12:00:00
# 2021-01-01 00:00:00
