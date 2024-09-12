# Lesson 12 - AND / OR Practice with IF statements
# January 24-25

# QUESTION 1: Individuals Martial Status 
'''
CustName = input("Enter Persons name: ")
MarStat =  input("Enter the Martial Status (S,M,W,D): ")
Age =      input("Enter the customer age: ")
Age  = int(Age)

Message = ""  # Referred to as a Null string 
if MarStat == "M":
    MarDate = input("Enter the marriage date (YYYY-MM-DD): ")
elif (MarStat == "W" or MarStat == "D") and Age > 40:
    Message = "Better get into a relationship quick."
# Put brackets around the "or" section when you have both 'or' AND 'and' operators. 


# Displaying the literals as well (Was stated in the problem)
if MarStat == "S":
    FullStatus = "Single"
elif MarStat == "M":
    FullStatus = "Married"
elif MarStat == "W":
    FullStatus = "Widowed"
else:
    FullStatus = "Divorced"

print(CustName)
print(Age)
print(FullStatus)
print(Message) 
# Because of the Null string, message will not print everytime unless W/D and >40 is inputted
# The Null string is ' variable = "" ' outside the "if" statement
'''

# QUESTION 2: Student ID and Student Grade
'''
StudNum =   input("Enter the student ID Number: ")
StudGrade = input("Enter the Student Grade (0-100): ")
StudGrade = int(StudGrade)

if StudGrade >= 90:
    LetterGrade = "A"
elif StudGrade <= 89 and StudGrade >= 80:
    LetterGrade = "B"
elif StudGrade <= 79 and StudGrade >= 70:
    LetterGrade = "C"
elif StudGrade <= 69 and StudGrade >= 60:
    LetterGrade = "D"
else:
    LetterGrade = "F"

print()
print("Letter Grade: " , LetterGrade)
'''

# QUESTION 3: Balance Due and Credit Limit 
'''
BalDue = input("Enter the Balance Due: ")
BalDue = float(BalDue)
CredLim = input("Enter the credit limit: ")
CredLim = float(CredLim)

Status = ""
if BalDue <= CredLim: 
    PaymentDue = BalDue * .10
else:
    PaymentDue = (BalDue * .10) + (BalDue - CredLim)

if BalDue <= CredLim:
    Status = "OK"
else:
    Status = "OVER"
    if BalDue > CredLim + 1000.00:
        Status = Status + "-CREDIT CHECK"

# I added this 'if' statement to the 'over' because the BalDue is essentially over. 
print()      
print(PaymentDue)
print(Status)
'''

# QUESTION 4: Home Mortagage / Loan Amount 
'''
LoanAmt = input("Enter the Loan amount: ")
LoanAmt = float(LoanAmt)

Deposit = 0 
Msg = ""
if LoanAmt < 25000.00:
    Deposit = LoanAmt * 0.05
elif LoanAmt >= 25000.00 and LoanAmt <= 49999.00:
    Deposit = 1250.00 + (LoanAmt - 25000.00) * .10  # Stated 'Loan over 25000' therefor, use subtraction
elif LoanAmt >= 50000.00 and LoanAmt <= 100000.00:
    Deposit = 5000.00 + (LoanAmt - 50000.00) * 0.25  # Same as above^
else:
    Msg = "Loan amount over 100000.00 are not allowed!"

print()
print("Deposit: " , Deposit)
print(Msg)
'''

# QUESTION 5: Museum Challenge 

FULL_PRICE = 22.50

print()
CurrDay = input("Enter the day of the week (M,T,W,Th,F,S,Su):  ")
Age =     input("Enter the customers age:                      ")
Age = int(Age)

print()
Msg = ""
Discount = ""
if CurrDay == "M":
    Msg = "We are closed on Monday"

elif CurrDay == "T" or CurrDay == "Th":
    Discount = FULL_PRICE * 0.5
    Msg = "Half off today!"

elif CurrDay == "W" and Age >= 13 and Age <= 20:
    Discount = FULL_PRICE * 0.25
    Msg = "You get a 25% price discount today!"

elif Age < 6 and Age > 65:
    Msg = "Your admission is free today"

elif CurrDay == "S" or CurrDay == "Su" and Age >= 6 and Age <= 12:
    Discount = FULL_PRICE * 0.5
    Msg = "You get a 50% price discount today!"
else:
    Msg = "You will have to pay full price of $22.50"

Total = FULL_PRICE - Discount

print("Current Day:                 " , CurrDay)
print("Customers Age:               " , Age)
print()
print("Price before discount:       " , FULL_PRICE)
print("Discount:                    " , Discount)
print("Total:                       " , Total)
print()
print("Message:                     " , Msg)
print()












