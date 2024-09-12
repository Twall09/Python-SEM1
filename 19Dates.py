# Introduction to DATES

# Define required libraries
import datetime

CurDate = datetime.datetime.now()
print(CurDate)

Today = "2024-02-07"
print(Today)

# These just display how the date are formatted
print(CurDate.strftime("%A, %a, %Y, %y, %m, %B, %b, %d,"))
print(CurDate.strftime("%B %d, %Y"))
print(CurDate.strftime("%A %B %d, %Y"))
print()

# Adding 4 days and 30 days to the current date.
# If days = -4, then it would subtract 4 days 

CurDatePlus4 = CurDate + datetime.timedelta(days = 4)
print("Current date plus 4 days")
print(CurDatePlus4)
print()
CurDatePlus30 = CurDate + datetime.timedelta(days = 30)
print("Current date plus 30 days")
print(CurDatePlus30)

# Define two dates as strings & convert to dates 
arrivalstr = "2021-2-3"
departurestr = "2021-2-6"

arrival = datetime.datetime.strptime(arrivalstr, "%Y-%m-%d")
print(arrival)

departure = datetime.datetime.strptime(departurestr, "%Y-%m-%d")
print(departure)

# Calculate the number of days between the departure and arrival 
days = (departure - arrival).days
print()
print(days)

# Subtracting a month from the current one given 
print()
CurYear = 2024
CurMonth = 4
CurDay = 24
LessAMonth = datetime.datetime(CurYear, CurMonth - 1, CurDay)
print(LessAMonth)


# EXAMPLE

while True:
    try:
        StartDate = input("Enter the start date (YYYY-MM-DD): ")
        StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    except:
        print("ERROR - Start date is not a valid format")
    else:
        break

while True:
    try:
        EndDate = input("Enter the end date (YYYY-MM-DD): ")
        EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
    except:
        print("ERROR - End date is not a valid format")
    else:
        break

# Calculations for example above 
NumDays = (EndDate - StartDate).days 
ClaimAmt = NumDays * 58.00
print()
print(NumDays)
print(ClaimAmt)