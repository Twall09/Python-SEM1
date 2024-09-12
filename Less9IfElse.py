# When doing a problem, usually the problem will state "if", therefore you will need to add this lesson. 
'''
if criteria:
    # Execute these statements if criteria is true
    statement(s)  # These indents are important for running the program
    statement(s)
else:
    # Execute these statements if criteria is false 
    statement(s)
    statement(s)
'''
# Example 1a: 
'''
Age = input("Enter a persons age: ")
Age = int(Age)

if Age >= 19: 
    print("Allowed to vote.")
# else statement is essentially the alternative or opposite of "if"
else:
    print("Too young to vote.")
'''

# Example 1b:
'''   
PayRate = 17.00  # 17.00 and 40 are just examples
HoursWorked = 40  # Take note that some people work 45, 50 whatever else hours.

if HoursWorked <= 40:
    GrossPay = HoursWorked * PayRate 
else:
    RegPay = 40 * PayRate
    OTHours = HoursWorked - 40
    OTRate = PayRate * 1.5 
    OTPay = OTHours * OTRate 
    GrossPay = RegPay + OTPay 

print(GrossPay)
'''
# Example 1c:
'''
Status = input("Enter the martial status (S,M,W,O): ").upper()  # .upper() allows the program to convert to uppercase letters.

if Status == "S": 
    print("Single")
# elif when there is more then 1 alternative. In this case, we have 2 (M,W).
# else becomes 'Other' because its not a labelled alternative
elif Status == "M":
    print("Married")
elif Status == "W":
    print("Widowed")
else:
    print("Other")
'''

# Example 1d:
'''
# These values are just examples 
BalDue = 2300.00 # input()
CredLim = 2000.00 # input()

if BalDue < CredLim:
    PayDue = BalDue * .10
else:
    PayDue = (BalDue * .10) + (BalDue - CredLim)

print(PayDue)
'''


