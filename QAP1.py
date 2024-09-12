# Description: Total Invoice for renting a vehicle from Edsel Car Rental Company
# QAP 1, Due January 17, 2024
# Author: Tyler Wall 
# Date: January 12, 2024

# Defining Constants 
PER_DAY_RATE = 55.00
PER_KM_RATE = .24
INS_RATE_DAY = 14.00
DIS_RENT_COST = .10
DIS_MILE_COST = .25
HST_RATE = .15

# Begin your program 

# Gather your inputs
CustName = input("Persons Name:")
PhoneNum = input("Enter the Phone Number:") # (999-999-9999) This is how I want my phone number to be displayed
NumDays = input("Number of Days Rented:")
NumDays = int(NumDays)
OdoRent = input("Odometer reading when rented:")
OdoRent = int(OdoRent) # Enter a 5 digit number 
OdoReturn = input("Odometer reading when returned:")
OdoReturn = int(OdoReturn) # Enter a 5 digit number 

print()
# Calculate the results 
TotalKm = OdoReturn - OdoRent 
RentCost = NumDays * PER_DAY_RATE
MilCost = TotalKm * PER_KM_RATE
InsCost = NumDays * INS_RATE_DAY
print()
DisRent = RentCost * DIS_RENT_COST
DisMil = MilCost * DIS_MILE_COST
TotalDis = DisRent + DisMil 
print()
TotalRentCost = RentCost + MilCost + InsCost - TotalDis
HST = TotalRentCost * HST_RATE 
InvoiceTotal = TotalRentCost + HST 

print()
# Displaying my results 
print("Persons Name: " , CustName)
print("Phone Number: " , PhoneNum)
print("Number of Days: " , NumDays)
print("Odometer Reading when rented: " , OdoRent)
print("Odometer reading when returned: " , OdoReturn)
print()
print("Total Kilometers: " , TotalKm)
print("Rental Cost: " , RentCost)
print("Mileage Cost: " , MilCost)
print("Insurance Cost: " , InsCost)
print()
print("Discount off rental cost: " , DisRent)
print("Discount off mileage cost: " , DisMil)
print("The total discount: " , TotalDis)
print("Total Rental cost: " , TotalRentCost)
print()
print("Taxes: " , HST)
print("Invoice Total: " , InvoiceTotal)