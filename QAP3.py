# QAP 3 
# Desciption: Honest Harrys car lot sales program 
# Author; Tyler Wall
# Date: February 7, 2024

# Define required libraries
import datetime

# Define Constants
LICENSE_FEE_LOW = 75.00
LICENSE_FEE_HIGH = 165.00
HST_RATE = 0.15
LUX_TAX_PRICE = 20000.00
LUX_TAX_RATE = 0.016
FINANCE_FEE = 39.99
TRANS_FEE_RATE = 0.01


# Gathering user inputs
print()
while True:
    
    CustFirst =  input("Enter the customers first name (END to quit):         ").title()
    if CustFirst.upper() == "END":
        print("Program has ended. Thank you and have a good day!")
        break

    while True:   
        CustLast =   input("Enter the customers last name:                        ").title()
        if CustLast == "":
            print("ERROR - Customer last name cannot be blank")
        else:
            break
        
        
    StAdd =          input("Enter the street address:                            ").title()
    City =           input("Enter the city:                                      ").title()
    Province =       input("Enter the province (XX):                             ").upper()
    PostCode =       input("Enter the postal code (X9X9X9):                      ").upper()
        

    while True:    
        PhoneNum =   input("Enter the customers phone number (9999999999):       ")
        if PhoneNum == "":
            print("ERROR - Phone Number cannot be blank")
        elif len(PhoneNum) != 10:     #len() is the length of the required input
            print("ERROR - Phone number must be 10 digits")
        elif PhoneNum.isdigit() == False: 
            print("Phone Number must be 10 numbers only")
        else:
            break
        
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz")
    allowed_num = set("1234567890")
    while True:     
        PlateNum =   input("Enter the customers plate number (XXX999):           ").upper()
        if len(PlateNum) != 6:
            print("ERROR - Plate number must be 6 characters")
        if set(PlateNum[0:3]).issubset(allowed_char) == False:
            print("ERROR - first 3 characters must be letters")
        elif set(PlateNum[3:6]).issubset(allowed_num) == False:
            print("ERROR - last 3 characters must be numbers")
        else:
            break
            
    CarMake =        input("Enter the car make:                                  ").title()
    CarModel =       input("Enter the car model:                                 ").title()
    Year =           input("Enter the year the car was made (9999):              ")
    Year = int(Year)

    while True:    
        try:
            SellingPrice =   input("Enter the selling price (99999.99):                  ")
            SellingPrice = float(SellingPrice)
        except:
            print("ERROR - Selling price is an invalid number")
        else:
            if SellingPrice > 50000.00:
                print("ERROR - Selling price must not exceed $50000.00")
            
        try:
            TradeAmt =       input("Enter the amount of the trade in:                    ")
            TradeAmt = float(TradeAmt)
        except:
            print("ERROR - Trade in amount is an invalid number")
        else:
            if TradeAmt > SellingPrice:
                print("ERROR - Trade in amount must not exceed the selling price")
            break
            
    SalesName =  input("Enter the salespersons name:                         ").title()
       

    # Calculations
        
    
    PriceAfter = (SellingPrice) - (TradeAmt)
            
    if SellingPrice <= 5000.00:
        LicenseFee = LICENSE_FEE_LOW
                
    else:
        LicenseFee = LICENSE_FEE_HIGH

    TransferFee = SellingPrice * TRANS_FEE_RATE

    if SellingPrice > LUX_TAX_PRICE:
        TransferFee = TransferFee + SellingPrice * LUX_TAX_RATE

    SubTotal = PriceAfter + LicenseFee + TransferFee
    HST = SubTotal * HST_RATE
    TotalSalesPrice = SubTotal + HST 
            
    ReceiptID = CustFirst[0] + CustLast[0] + "-" + PlateNum[3:6] + "-" + PhoneNum[6:10]

    # Display my results 
    
    print()
        
    CurDateStr = "2024-02-09"
    CurDate = datetime.datetime.strptime(CurDateStr, "%Y-%m-%d")
    print(f"Honest Harry Car Sales                     Invoice Date: {CurDate.strftime("%B %d, %Y")}")
    print(f"Used Car Sale and Receipt                  Receipt No:         {ReceiptID:>11s}")
        
    print()
    SellingPriceDsp = "${:,.2f}".format(SellingPrice)
    print(f"                                       Sale Price:              {SellingPriceDsp:>10s}")
                
    TradeAmtDsp = "${:,.2f}".format(TradeAmt)
    print(f"Sold to:                               Trade Allowance:         {TradeAmtDsp:>10s}")
    print(f"                                       -----------------------------------")
                
    PriceAfterDsp = "${:,.2f}".format(PriceAfter)
    print(f"     {CustFirst[0] + ". "}{CustLast}                           Price after Trade:       {PriceAfterDsp:>10s}")
                
    LicenseDsp = "${:,.2f}".format(LicenseFee)
    print(f"     {StAdd + " - "}{PhoneNum}       License Fee:             {LicenseDsp:>10s}")
                
    TransferDsp = "${:,.2f}".format(TransferFee)
    print(f"     {City}, {Province} {PostCode}               Transfer Fee:            {TransferDsp:>10s}")
    print(f"                                       -----------------------------------")
                
    SubTotDsp = "${:,.2f}".format(SubTotal)
    print(f"Car Details:                           Subtotal:                {SubTotDsp:>10s}")
                
    HSTDsp = "${:,.2f}".format(HST)
    print(f"                                       HST:                     {HSTDsp:>10s}")
    print(f"     {Year} {CarMake} {CarModel}             -----------------------------------")
                
    TotalSaleDsp = "${:,.2f}".format(TotalSalesPrice)
    print(f"                                       Total Sales Price:       {TotalSaleDsp:>10s}")
    print()
    print(f"--------------------------------------------------------------------------")
                
    print()
    print(f"                                Financing       Total          Monthly")
    print(f"   # Years      # Payments         Fee          Price          Payment")
    print(f"  --------------------------------------------------------------------")

    for Years in range(1,5):
        NumPayments = Years * 12
        Financing = Years * FINANCE_FEE
        TotalPrice = TotalSalesPrice + Financing
        MonPayment = TotalPrice / NumPayments

        FinanceDsp = "${:,.2f}".format(Financing)
        TotPriceDsp = "${:,.2f}".format(TotalPrice)
        MonPayDsp = "${:,.2f}".format(MonPayment)

        print(f"      {Years:>2d}            {NumPayments:>2d}          {FinanceDsp:>7s}       {TotPriceDsp:>10s}     {MonPayDsp:>9s}")
        

        FirstDate = CurDate + datetime.timedelta(days = 30)
        FirstDate = datetime.datetime.strftime(FirstDate, "%d-%b-%y")
        
    
    print(f"  --------------------------------------------------------------------")
    print(f"  Invoice Date: {CurDate.strftime("%d-%b-%y")}                First payment date: {FirstDate}")
    print()
    
    # HOUSEKEEPING
    print(f"--------------------------------------------------------------------------")
    print(f"                  Best used cars at the best prices!                         ")
    print()
 


        




        
    
        