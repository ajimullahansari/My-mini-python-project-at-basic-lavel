import calendar

year = int(input("Enter year here:"))
month = int(input("Enter month here:"))

calendar = calendar.month(year,month)
print(calendar)