from datetime import datetime

date = datetime(2021, 4, 20, 11, 30, 0)

print(date.strftime("%Y-%m-%d"))
print(date.strftime("%d-%m-%Y"))
print(date.strftime("%m-%Y"))
print(date.strftime("%B-%Y"))
print(date.strftime("%d %B, %Y"))
print(date.strftime("%Y-%m-%d %H:%M:%S"))
print(date.strftime("%m/%d/%y %H:%M:%S"))
print(date.strftime("%d(%a) %B %Y"))

date_str_1 = "3 March 1995"
date_str_2 = "3/9/1995"
date_str_3 = "21-07-2021"

print(datetime.strptime(date_str_1, "%d %B %Y"))
print(datetime.strptime(date_str_2, "%d/%m/%Y"))
print(datetime.strptime(date_str_3, "%d-%m-%Y"))
