# QAP 2 - Python Programming
# Description: Preparing a receipt for the St.John's Marina and Yaht Club
# Author: Tyler Wall
# Date: January 31st, 2024

# Define Constants

EVEN_SITE_RATE = 80.00
ODD_SITE_RATE = 120.00
ALT_MEM_RATE = 5.00
SITE_CLEAN = 50.00
VIDEO_SURV = 35.00
HST_RATE = 0.15
STAND_MEM = 75.00
EXEC_MEM = 150.00
PROCESS_FEE = 59.99
CANCEL_FEE = 0.60

# Gathering user inputs 
print()
CurrDate =     input("Enter the current date (YYYY-MM-DD):                    ")
SiteNum =      input("Enter the site number (1 - 100):                        ")
SiteNum = int(SiteNum)
MemName =      input("Enter the member's name:                                ")
StAdd =        input("Enter the street address:                               ")
City =         input("Enter the city:                                         ")
Province =     input("Enter the province (XX):                                ")
PostalCode =   input("Enter the Postal code (X9X9X9):                         ")
PhoneNum =     input("Enter your home phone number (999-999-9999):            ")
CellNum =      input("Enter your cell phone number (999-999-9999):            ")
MemType =      input("Enter your membership type (S / E):                     ")
NumAltMem =    input("Enter the number of alternate members:                  ")
NumAltMem = int(NumAltMem)
WeekClean =    input("Would you like weekly site cleaning (Y / N):            ")
VidSur =       input("Would you like video surveillance (Y / N):              ")

# Calculations 

SiteRate = 0
if SiteNum % 2 == 0:
    SiteRate += EVEN_SITE_RATE
else:
    SiteRate += ODD_SITE_RATE

SiteChrg = SiteRate + NumAltMem * ALT_MEM_RATE

if WeekClean == "Y" and VidSur == "Y":
    ExtraChrg = SITE_CLEAN + VIDEO_SURV
elif WeekClean == "Y" and VidSur == "N":
    ExtraChrg = SITE_CLEAN
elif WeekClean == "N" and VidSur == "Y":
    ExtraChrg = VIDEO_SURV
else:
    ExtraChrg = 0

if WeekClean == "Y":
    CleanDsp = "Yes"
else:
    CleanDsp = "No"

if VidSur == "Y":
    VidDsp = "Yes"
else:
    VidDsp = "No"

if MemType == "S":
    MonthlyDues = STAND_MEM
    MemType = "Standard"
else:
    MonthlyDues = EXEC_MEM
    MemType = "Executive"

SubTotal = SiteChrg + ExtraChrg
HST = SubTotal * HST_RATE
TotMonthChrg = SubTotal + HST 

TotalFee = TotMonthChrg + MonthlyDues
TotYearlyFee = TotalFee * 12 

MonthPayment = (TotYearlyFee + PROCESS_FEE) / 12

Cancellation = (SiteChrg * 12) * CANCEL_FEE 

# Display my results 

print()
print("     St. John's Marina & Yacht Club    ")
print("          Yearly Member Receipt    ")
print()
print(f"-------------------------------------------")
print()
print("Client Name and Address: ")
print()
print(MemName)
print(StAdd)
print(f"{City}, {Province}, {PostalCode}")
print()
print(f"Phone: {PhoneNum} (H)")
print(f"       {CellNum} (C)")
print()
print(f"Site #:  {SiteNum}           Member type: {MemType}")
print()
print(f"Alternate members:                       {NumAltMem}")
print(f"Weekly site cleaning:                  {CleanDsp}")
print(f"Video surveillance:                     {VidDsp}")
print()
SiteChrgDsp = "${:,.2f}".format(SiteChrg)
print(f"Site charges:                    {SiteChrgDsp:>9s}")
ExtraChrgDsp = "${:,.2f}".format(ExtraChrg)
print(f"Extra charges:                     {ExtraChrgDsp:>7s}")
print(f"                               ------------")
SubTotalDsp = "${:,.2f}".format(SubTotal)
print(f"Subtotal:                        {SubTotalDsp:>9s}")
HSTDsp = "${:,.2f}".format(HST)
print(f"Sales tax (HST):                   {HSTDsp:>7s}")
print(f"                               ------------")
TotMonDsp = "${:,.2f}".format(TotMonthChrg)
print(f"Total monthly charges:           {TotMonDsp:>9s}")
MonDueDsp = "${:,.2f}".format(MonthlyDues)
print(f"Monthly Dues:                      {MonDueDsp:>7s}")
print(f"                               ------------")
TotFeeDsp = "${:,.2f}".format(TotalFee)
print(f"Total monthly fees:              {TotFeeDsp:>9s}")
YearlyDsp = "${:,.2f}".format(TotYearlyFee)
print(f"Total yearly fees:              {YearlyDsp:>10s}")
print()
MonPayDsp = "${:,.2f}".format(MonthPayment)
print(f"Monthly payment:                   {MonPayDsp}")
print()
print(f"-------------------------------------------")
print()
print(f"Issued: {CurrDate}")
print("HST Reg No:      549-33-5849-4720-9885")
print()
CancelDsp = "${:,.2f}".format(Cancellation)
print(f"Cancellation fee:                {CancelDsp:>9s}")
print()