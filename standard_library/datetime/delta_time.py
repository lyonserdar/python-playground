"""
delta_time.py
"""
import datetime

date = datetime.datetime(2020, 1, 1)

# Create a new object by adding a delta time to date
print(date + datetime.timedelta(days=7))
print(date + datetime.timedelta(hours=30))
print(date + datetime.timedelta(minutes=15))
print()

# Create a timedelta object that can be used to get incremental date objects
delta = datetime.timedelta(hours=8)
dates = [date + i * delta for i in range(12)]

for date in dates:
    print(date)

# OUTPUT
# 2020-01-08 00:00:00
# 2020-01-02 06:00:00
# 2020-01-01 00:15:00

# 2020-01-01 00:00:00
# 2020-01-01 08:00:00
# 2020-01-01 16:00:00
# 2020-01-02 00:00:00
# 2020-01-02 08:00:00
# 2020-01-02 16:00:00
# 2020-01-03 00:00:00
# 2020-01-03 08:00:00
# 2020-01-03 16:00:00
# 2020-01-04 00:00:00
# 2020-01-04 08:00:00
# 2020-01-04 16:00:00
