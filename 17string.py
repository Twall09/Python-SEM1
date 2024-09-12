# DIFFERENT WAYS TO FORMAT STRINGS

'''
Name = "seamus o'toole-melanson"

UName = Name.upper()  # Upper cases the whole word 
print(UName)

CName = Name.capitalize()  # Capitalizes first letter of first word only 
print(CName)

TName = Name.title()  # Capitalizes first letter of each word 
print(TName)

Title = "Mr."
FirstName = "John"
LastName = "Doe"

# Display as "Mr. John Doe"
FName1 = Title + " " + FirstName + " " + LastName
print(f"Customer Name:         {FName1:<20s}")

# Display as "J.Doe"
FirstLetter = FirstName[0]
print(FirstLetter)

FName2 = FirstName[0] + ". " + LastName
print(FName2)

# Display as "Doe, John
FName3 = LastName + ", " + FirstName
print(FName3)

print()
'''
# EXAMPLE 2
'''
import random 

DeptName = input("Enter the department name: ")
DeptName = DeptName.title()
print(DeptName)

CurrDate = "2024-02-05"
FirstName = "Cory"
LastName = "Williams"
LocCode = "AJRD"
TransCode = 14974
CustCtr = random.randint(1000, 10000) # Generates a random number between the 2 

TransCodeStr = str(TransCode)   # Need to convert these int's to strings 
CustCtrStr = str(CustCtr)
TrackNum = FirstName[0] + LastName[0] + "-" + LocCode[0:2] + "-" + TransCodeStr[3:5] + "-" + CurrDate[0:4] + CustCtrStr
print(TrackNum)
'''

# EXAMPLE 3 - VALIDATIONS 
'''
while True:
    CCNum = input("Enter the credit card number (9999999999999999): ")

    if len(CCNum) != 16:
        print("ERROR - CC Num needs to be 16 characters")
    elif CCNum.isdigit() == False:
        print("ERROR - CC Num must be all numbers") 
    elif CCNum[0] != "4" and CCNum[0] != "5":
        print("ERROR - Visa must start with 4, Mastercard must start with 5")
    else:
        break

CCNum = CCNum[0:4] + " " + CCNum[4:8] + " " + CCNum[8:12] + " " + CCNum[12:16]
print(CCNum)
'''

# ANOTHAAA ONE 
'''
allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
allowed_num = set("1234567890")
while True:
    PlateNum = input("Enter the plate number (XXX999): ").upper()

    if len(PlateNum) != 6:
        print("ERROR - Plate number must be 6 characters")
    if set(PlateNum[0:3]).issubset(allowed_char) == False:
        print("ERROR - first 3 characters must be letters")
    elif set(PlateNum[3:6]).issubset(allowed_num) == False:
        print("ERROR - last 3 characters must be numbers")
    else:
        break

print(PlateNum)
'''

# AYOOO WE MOVIN'

allowed_upper_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
allowed_lower_char = set("abcdefghijklmnopqrstuvwxyz")
allowed_num = set("1234567890")
UpperCtr = 0
LowerCtr = 0
NumCtr = 0
SpecCtr = 0
while True:
    Password = input("Enter a password: ")

    for Char in Password:   # Process each letter one at a time
        if set(Char).issubset(allowed_upper_char) == True:
            UpperCtr += 1
        elif set(Char).issubset(allowed_lower_char) == True:
            LowerCtr += 1
        elif set(Char).issubset(allowed_num) == True:
            NumCtr += 1
        else:
            SpecCtr += 1 

    print(UpperCtr)
    print(LowerCtr)
    print(NumCtr)
    print(SpecCtr)
    
    if  len(Password) < 7:
        print("ERROR - Password must have at least 7 characters")
    elif UpperCtr == 0:
        print("ERROR - Password must contain at least 1 uppercase character")
    elif LowerCtr == 0:
        print("ERROR - Password must contain at least 1 lowercase character")
    elif NumCtr == 0:
        print("ERROR - Password must contain at least 1 number")
    elif SpecCtr == 0:
        print("ERROR - Password must contain at least 1 special character")
    else:
        break


    
        

