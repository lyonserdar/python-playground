import datetime

date = datetime.datetime(2020, 1, 1)

print(date + datetime.timedelta(days=7))
print(date + datetime.timedelta(hours=30))
print(date + datetime.timedelta(minutes=15))

delta = datetime.timedelta(hours=8)

dates = [date + i * delta for i in range(12)]

for date in dates:
    print(date)
