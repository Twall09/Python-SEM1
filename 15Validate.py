# Comment like a pro.

# Import Libraries

# Define constants

# Define functions  

# Main Program 
while True:
    # Gather inputs
    while True: 
        FirstName = input("Enter the customers first name: ")

        if FirstName == "":
            print("Data Entry Error - Customer first name cannot be blank.")
        else:
            break 
    
    while True:
        try:  # The try checks to make sure the number is valid 
            NumWeeks = input("Enter the number of weeks (1-4): ")
            NumWeeks = int(NumWeeks)
        except:
            print("Data entry error - Number of weeks is not a valid number.")
        else:
            if NumWeeks < 1 or NumWeeks > 4:
                print("Data entry error = Number of weeks must be between 1 - 4.")
            else:
                break
    
    while True:
        try:
            CostWeek = input("Enter the cost per week: ")
            CostWeek = float(CostWeek)
        except:
            print("Data Entry Error - Cost per week is an invalid number")
        else:
            break

    
    while True: 
        ConFlight = input("Do you need a connector flight to Toronto (Y/N): ").upper()

        if ConFlight == "":
            print("Data entry error - connection flight cannot be blank.")
        elif ConFlight != "Y" and ConFlight != "N":
            print("Data Entry error - connection flight must be Y or N.")
        else:
            break 


    # Perform Calculations

    
    # Display Results
        print()
    while True:
        Continue = input("Do you want to process another vacation (Y/N)?: ").upper()
            
        if Continue == "":
                print("Data Error")
        elif Continue != "Y" and Continue != "N":
                print("Data Error")
        else:
                break

    if Continue == "N":
        break
               

# Housekeeping
print()
print("Thank you for your time. Have a good day.") 
print()