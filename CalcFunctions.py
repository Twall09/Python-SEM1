# Description: 
# Author: 
# Date(s):

# Define Libraries
import datetime
import FormatValues as FV  # as FV allows the printed formatted values to work.

# Define Constants
BASE_SALARY = 350.00
SALES_QUOTA = 5000.00

TODAY = datetime.datetime.now()

# Define Functions

def DetLetterGrade(NumGrade):
    # Determine and return a letter grade

    if NumGrade >= 80:
        LetterGrade = "A"
    elif NumGrade >= 70 and NumGrade <= 79:
        LetterGrade = "B"
    elif NumGrade >= 60 and NumGrade <= 69:
        LetterGrade = "C" 
    elif NumGrade >= 50 and NumGrade <= 59:
        LetterGrade = "D"
    else:
        LetterGrade = "F"

    return LetterGrade 



def CalcWeekGrossPay(Hours, PayRate):
    # Determine and return the weekly gross pay for an employee 
    # Based on hours worked and hourly pay rate 

    if Hours <= 40:
        GrossPay = Hours * PayRate
    else:
        RegPay = PayRate * 40
        OTPay = (Hours - 40) * (PayRate * 1.5)
        GrossPay = RegPay + OTPay

    return GrossPay


def CalcEmpBonus(TotalSales): 
    # Determine the total sales of an employee and return the bonus

    Bonus = TotalSales * 0.01

    if TotalSales < 5000.00:
        Bonus = 0
    elif TotalSales > 100000.00:
        Bonus += 500.00
    
    return Bonus



def CalcSumofValues(Number):
    # Determine the sum of digits upto a specified value 
    Total = 0
    for i in range(0, Number + 1):
        Total += i 
    
    return Total


def CalcPayDate(PurDate):
    # Determine the payment date as the first day of the next month 


    PurYear = PurDate.year
    PurMonth = PurDate.month
    PurDay = PurDate.day 

    PayYear = PurYear 
    PayMonth = PurMonth + 1
    if PayMonth > 12:
        PayMonth -= 12
        PayYear += 1
    PayDay = 1

    if PurDay >= 25:
        PayMonth += 1
        if PayMonth > 12:
            PayMonth -= 12
            PayYear += 1

    PayDate = datetime.datetime(PayYear, PayMonth, PayDay)

    return PayDate


def CalcGPDraw(EmpSales):
    # Calculate the gross pay based on a draw against commission

    if EmpSales >= SALES_QUOTA:
        Comm = EmpSales * .04
        GrassPay = BASE_SALARY + Comm
    else:
        Draw = (SALES_QUOTA - EmpSales) * 0.10
        GrassPay = BASE_SALARY - Draw

    if EmpSales > 20000.00:
        GrassPay += 500.00
    elif EmpSales > 10000.00:
        GrassPay += 200.00

    return GrassPay


def DetCustStatus(BalDue, CredLim, LastPurDate, LastPayDate):
    # Determine a customer status based on balance, and days between last purchase date and last payment date

    if BalDue <= CredLim:
        Status = "OK"
    if BalDue < CredLim and BalDue + 200 > CredLim:
        Status = "CHECK"
    elif BalDue > CredLim:
        Status = "OVER"

    DaysLastPur = (TODAY - LastPurDate).days
    if DaysLastPur > 60:
        Status += " - PURCH"

    DaysLastPay = (TODAY - LastPayDate).days
    if DaysLastPay > 30:
        Status += " - PAY"

    return Status


def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.
    # I incorperated this into the question above

    DollarValueStr = "${:,.2f}".format(DollarValue)
    return DollarValueStr


# Main Program 
while True:

    # Gather Inputs
    print()
    # Question 1 
    NumGrade = input("Enter the numeric grade (0 - 100): ")
    NumGrade = int(NumGrade)

    # Question 2 
    HoursWorked = 35
    HourlyPayRate = 15.00  # Would usually make these inputs
    
    # Question 3 
    Sales = 145000

    # Question 4
    Number = 10

    # Question 5
    PurDate = "2024-11-27"
    PurDate = datetime.datetime.strptime(PurDate, "%Y-%m-%d")

    # Quesion 6
    TotMonthlySales = 11000.00

    # Question 7
    BalDue = 300.00
    CredLim = 2000.00

    LastPurDate = "2023-12-27"
    LastPurDate = datetime.datetime.strptime(LastPurDate, "%Y-%m-%d")
    LastPayDate = "2024-08-15"
    LastPayDate = datetime.datetime.strptime(LastPayDate, "%Y-%m-%d")
    
    
    # Calculations
    #1
    LetterGrade = DetLetterGrade(NumGrade)

    #2
    WeeklyGrossPay = CalcWeekGrossPay(HoursWorked, HourlyPayRate)

    #3 
    Bonus = CalcEmpBonus(Sales)

    #4
    Total = CalcSumofValues(Number)

    #5
    PayDate = CalcPayDate(PurDate).date()

    #6
    GrassPay = CalcGPDraw(TotMonthlySales)

    #7
    Status = DetCustStatus(BalDue, CredLim, LastPurDate, LastPayDate)
    # I formatted  these dollar values and printed them below.

    # Display Results
    print("Letter Grade:       " , LetterGrade)
    print("Weekly Gross Pay:   " , WeeklyGrossPay)
    print("Bonus Value:        " , Bonus)
    print("Sum of Value:       " , Total)
    print("Pay date:           " , PayDate) 
    print("Grass Pay:          " , GrassPay)
    print("Status:             " , Status)
    print()
    print(f"   Balance Due:           {FV.FDollar2(BalDue):>10s}")
    print(f"   Credit Limit:          {FV.FComma2(CredLim):>10s}")
    print(f"   Todays Date:           {FV.FDateS(TODAY):>10s}")
    print(f"   Todays Date:           {FV.FDateM(TODAY):>10s}")
    print(f"   Todays Date:           {FV.FDateL(TODAY):>19s}")

    Wait = input("Press ENTER to continue.")
    # Once FormatValues is imported, in your print statements you can actually change the display from functions that are in another program (FormatValues.py)



# Housekeeping 