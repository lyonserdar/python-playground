"""
date_formatting.py
"""
from datetime import datetime

date = datetime(2021, 4, 20, 11, 30, 0)

#  Formats the dates
print(date.strftime("%Y-%m-%d"))
print(date.strftime("%d-%m-%Y"))
print(date.strftime("%m-%Y"))
print(date.strftime("%B-%Y"))
print(date.strftime("%d %B, %Y"))
print(date.strftime("%Y-%m-%d %H:%M:%S"))
print(date.strftime("%m/%d/%y %H:%M:%S"))
print(date.strftime("%d(%a) %B %Y"))
print()

date_str_1 = "3 March 1995"
date_str_2 = "3/9/1995"
date_str_3 = "21-07-2021"

# Creates objects from different date strings
print(datetime.strptime(date_str_1, "%d %B %Y"))
print(datetime.strptime(date_str_2, "%d/%m/%Y"))
print(datetime.strptime(date_str_3, "%d-%m-%Y"))

# OUTPUT
# 2021-04-20
# 20-04-2021
# 04-2021
# April-2021
# 20 April, 2021
# 2021-04-20 11:30:00
# 04/20/21 11:30:00
# 20(Tue) April 2021

# 1995-03-03 00:00:00
# 1995-09-03 00:00:00
# 2021-07-21 00:00:00
