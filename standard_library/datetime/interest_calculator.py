import datetime

rate = 0.04
pv = 1000
daily_rate = rate / 365.0

d1 = datetime.date(2021, 7, 1)
d2 = datetime.date(2021, 12, 31)
num_of_days = (d2 - d1).days

fv = pv * (1 + daily_rate) ** num_of_days

print(f"Furute value: ${fv:.2f}")
