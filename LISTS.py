# Description
# Author
# Date

# TUPLE is enclosed is () and a LIST is [].

# Define reuired libraries
import FormatValues as FV 
import datetime

# Define Constants


# Define Functions
def CalcBonusStatus(TotalSales):
    # Calculate the employee bonus and status 

    Bonus = TotalSales * .01
    if TotalSales < 5000.00:
        Less = (TotalSales - 5000.00) * .17
        Bonus -= Less
        Status = "Under"
    elif TotalSales >= 5000.00 and TotalSales <= 100000.00:
        Status = "Normal"
    elif TotalSales > 100000.00:
        Bonus += 500.00
        Status = "Extraordinary"
    
    return Bonus, Status
    # Returned in round brackets and as a tuple. Non-editable list


# Main Program 


# Initialize my TO-DO List 
'''
ToDoLst = ["Take out the garbage", "Study Essentials", "Write Python Program"]
                #0                       1                      2 

print(ToDoLst)
print(ToDoLst[1])  # Elements [1] for example, are always inputted with square brackets

print()
NewItem = input("Enter a new item for the ToDo list: ")
ToDoLst.append(NewItem)
print(ToDoLst)
# append feature adds an item to the end of the list



# Display the list

print()
print("ToDo list for T")
print("----------------------")
ListCtr = 0
for Job in ToDoLst:
    print(f"  {ListCtr:<1d}. {Job}")    # ListCtr displays it in a ordered list
    ListCtr += 1
print("----------------------")

DelItem = input("Enter the item to remove: ")
DelItem = int(DelItem)

ToDoLst.__delitem__(DelItem)
# Can also use ToDoLst.pop() to delete the last item in the list

print()
print("ToDo list for T")
print("----------------------")
ListCtr = 0
for Job in ToDoLst:
    print(f"  {ListCtr:<1d}. {Job}")    
    ListCtr += 1
print("----------------------")


# EXAMPLE 
NumberLst = []
while True:
    Number = input("Enter a number (-1 to end): ")
    Number = int(Number)
    if Number == -1:
        break

    NumberLst.append(Number)

print(NumberLst)


# EXAMPLE

ProvList = ["NL", "NS", "NB", "PEI", "QC", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
while True:
    Prov = input("Enter the customer province (XX): ").upper()
    if Prov == "":
        print("ERROR - cannot be blank")
    elif len(Prov) != 2:
        print("ERROR - must be only 2 characters")
    elif Prov not in ProvList:
        print("ERROR - Invalid province")
    else:
        break
        

EmpBonSta = CalcBonusStatus(40000.00)
print()
print(EmpBonSta)
print()
Bonus = EmpBonSta[0]
Status = EmpBonSta[1]
print(Bonus)
print(Status)
'''

# EXAMPLE
while True:
    print()
    ListNo = input("Enter the listing number (999999999): ")
    StAdd = input("Enter the street address: ")
    NumBedRooms = input("Enter the number of bedrooms: ")
    NumBedRooms = int(NumBedRooms)
    NumBathRooms = input("Enter the number of bathrooms: ")
    NumBathRooms = float(NumBathRooms)
    TotSqFt = input("Enter the total square footage: ")
    TotSqFt = int(TotSqFt)
    
    ListPriceLst = []
    ListDateLst = []
    while True:
        ListPrice = input("Enter the listing price (-1 to end): ")
        ListPrice = float(ListPrice)
        if ListPrice == -1:
            break

        ListDate = input("Enter the listing date: ")
        ListDate = datetime.datetime.strptime(ListDate, "%Y-%m-%d")

        ListPriceLst.append(ListPrice)
        ListDateLst.append(ListDate)

    StatusList = ["Open", "Offer Pending", "Sold"]
    while True:
        Status = input("Enter the current status (Open, Offer Pending, Sold): ").title()
        if Status == "":
            print("Error - Invalid entry")
        elif Status not in StatusList:
            print("Error - Entry must be one of those in list")
        else:
            break
    
    # Calculations
    # Display Results
    print(StAdd)
    print(TotSqFt)
    print()
    print("  List Price         List Date")
    print("  ----------------------------")

    PriceIndex = 0
    for Price in ListPriceLst:
        print(f"  {FV.FDollar2(ListPriceLst[PriceIndex]):>14s}    {FV.FDateM(ListDateLst[PriceIndex]):>9s}")
        PriceIndex += 1

    print("  ----------------------------")



