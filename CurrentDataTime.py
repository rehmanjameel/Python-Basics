from datetime import datetime
from datetime import date
import calendar


# Get the current dat
today = date.today()
print("Today's date: ", today)

# Current date simple format
d1 = today.strftime("%d/%m/%Y")
print(d1)

# Current date time format with full month name
d2 = today.strftime("%B %d, %Y")
print(d2)

# Get the current date and time
now = datetime.now()
print(now)

# current date time simple format
dtString = now.strftime("%d/%m/%Y %H:%M:%S")
print(dtString)

# Input the month number to get the month name
monthNum = int(input("Enter the month no: "))

# Passing the month number
datTimeObject = now.strptime(str(monthNum), "%m")

# Get the month name in short form
shortMonthName = datTimeObject.strftime("%b")
print(shortMonthName)

# Get the month name in full form
monthName = datTimeObject.strftime("%B")
print(monthName)

for i in range(1, 13):
    print(i, ":", calendar.month_abbr[i], "-", calendar.month_name[i])