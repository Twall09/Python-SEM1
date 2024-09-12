# Description; Program for Billy Bob bike rentals 
# Author: Tyler Wall
# Date: Feb 1

while True:

    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz")
    while True:
        CustName = input("Enter the customers name: ")
        
        if CustName == "":
            print("ERROR - Customer name cannot be blank")
        elif set(CustName).issubset(allowed_char) == False:
            print("Customer name includes invalid characters")
        else:
            break

    while True:
        PhoNum = input("Enter the phone number (9999999999): ")
        if PhoNum == "":
            print("ERROR - Phone Number cannot be blank")
        elif len(PhoNum) != 10:   #len() is the length of a string
            print("ERROR - Phone number is 10 digits only")
        elif PhoNum.isdigit() == False: 
             print("Phone Number must be 10 numbers only")
        else:
            break

    while True:
        CodeBike = input("Enter a code for the type of bike (T, M, B): ").upper()
        if CodeBike == "":
            print("ERROR - code entry cannot be blank")
        elif CodeBike != "T" and CodeBike != "M" and CodeBike != "B":
            print("ERROR - Bike type is an invalid entry")
        else:
            break
    
    while True:
        try:   # Try is inserted becasue of the numerical value
            NumBikes = input("Enter the number of bikes (1 - 3): ")
            NumBikes = int(NumBikes)
        except:
            print("ERROR - Number of bikes rented is not a valid number. ")
        else:
            if NumBikes < 1 or NumBikes > 3:
                print("ERROR - Number of bikes must be between 1 and 3")
            else:
                break

    CCNum = input("Enter the credit card number (9999999999999999): ")
    ExpDate = input("Enter the credit card expiry date (MM/YY): ").upper()

    
    print()
    while True:
        Continue = input("Do you want to process another bike rental (Y/N)?: ").upper()
            
        if Continue == "":
                print("Data Error")
        elif Continue != "Y" and Continue != "N":
                print("Data Error")
        else:
                break

    if Continue == "N":
        break
               
    

        
    