# Description: INTRO TO FUNCTIONS
# Author:
# Date:

# Define Libraries
import datetime

# Define Constants
  
CUR_DATE = datetime.datetime.now()

# Counters for the program
global TempCtr, THRCtr, SantaCtr, OldInvCtr, GuessCtr
TempCtr = 0
THRCtr = 0
SantaCtr = 0
OldInvCtr = 0
GuessCtr = 0

# Define Functions
'''
def RepeatThis():
    print("This is the code thats repeated")

def RepeatThat():
    print("This is another repeated code")

# Main Program
while True:

    A = input("Enter a value: ")
    A = int(A)
    B = input("Enter a value: ")
    B = int(B)
    # To call a function, you reference it by name
    RepeatThis()

# Calculations
    C = A + B
    D = A * B
    RepeatThis()

# Display 
    print(A)
    print(B)
    RepeatThis()
    RepeatThat()
    print(C)
    print(D)
    '''
# Mo's MAIN MENU Example from Lesson 21
while True:


    def ConvCelToFahr():
            # Function to convert a temp from celsius to
            # Fahrenheit and display the results.

        global TempCtr # Needs to be defined as global inside the function 
            
        TempCel = input("Enter the temperature in celsius: ")
        TempCel = int(TempCel)
        TempFahr = (9 / 5 * TempCel) + 32
        print(f"A temperature of {TempCel} celsius is equal to {TempFahr} fahrenheit.")

        TempCtr += 1
            
            # After a function is complete, it returns to the
            # end of the statement where it was called, and continues
            # with the rest of the program.
        
    def DetTHR():
            pass
    def DaysToCmas():
            pass
    def DetInvAge():
            pass # Determine the age and status of an invoice
            
            global OldInvCtr, CUR_DATE
        
    CompName = input("Enter the company name: ").title()
    InvDate = input("Enter the invoice date (YYYY-MM-DD): ")
    InvDate = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
    InvAmt = input("Enter the invoice amount: ")
    InvAmt = float(InvAmt)

    Age = (CUR_DATE - InvDate).days
    CUR_DATE = CUR_DATE + datetime.timedelta(days=10)

    if Age <= 30:
        Status = "OK"
    elif Age >= 31 and Age <= 60:
        Status = "Better think about paying"
    else:
        Status = "Could be in trouble"

        print("Age:        ", Age)
        print("Status:     ", Status)

        OldInvCtr += 1 



    def PlayGuessGame():
        pass
        
    while True:
        print()
        print("Mo’s Quick Problems - Main Menu")
        print(f"Date: {CUR_DATE}")
        print(f"Sessions totals:  Temperature: {TempCtr} THR: {THRCtr} Days to Santa: {SantaCtr} Old Invoice: {OldInvCtr} Guess: {GuessCtr}")
        print()
        print("1. Convert Celsius to Fahrenheit.")
        print("2. Determine Training Heart Rate.")
        print("3. How many days to Christmas?")
        print("4. How old is an invoice?")
        print("5. Play my guessing game.")
        print("6. Quit")
        print()
        
        while True:
            try:
                Choice = input("Enter choice (1 - 6): ")
                Choice = int(Choice)
            except:
                    print("Data Entry Error - must be a valid number between 1 and 6.")
            else:
                if Choice < 1 or Choice > 6:
                        print("Data Entry Error - must be a valid number between 1 and 6.")
                else:
                    break
            
        if Choice == 1:
                ConvCelToFahr()
        elif Choice == 2:
                DetTHR()
        elif Choice == 3:
                DaysToCmas()
        elif Choice == 4:
                DetInvAge()
        elif Choice == 5:
                PlayGuessGame()
        else:
            break
        
        # Any housekeeping duties at the end of the program.
        print()

    print("Thanks for using Mo's Quick Problems.")
