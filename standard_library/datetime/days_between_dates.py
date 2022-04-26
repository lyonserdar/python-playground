import datetime

d1 = datetime.date(2020, 7, 21)
d2 = datetime.date(2020, 12, 31)
days_between_dates = (d2 - d1).days
print(f"Number of days: {days_between_dates}")

d1 = datetime.datetime(2020, 7, 20, 11, 30, 0)
d2 = datetime.datetime(2021, 2, 20, 10, 25, 0)
time_between_dates = d2 - d1
print(f"Number of days: {time_between_dates}")

today = datetime.date.today()
end_of_year = datetime.date(today.year, 12, 31)
diff = (end_of_year - today).days
print(f"Number of days until the end of the year: {diff}")

now = datetime.datetime.now()
end_of_year = datetime.datetime(now.year + 1, 1, 1)
diff = end_of_year - now
print(f"Until the end of the year: {diff}")
