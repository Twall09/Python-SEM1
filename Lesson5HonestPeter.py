DateProcessed = "02-14-98"
InvoiceNum = "1234"
Customer = "Mark Wall"
Address = "58 Dawg Place"
City = "Paradise, NL, A1l2P4"

PlateNum = "A1X2W9"
Mileage = 117009
CostLabor = 250.00
CostParts = 300.00
TotalDiscount = 75.00
HST = 82.50
InvoiceTotal = 557.50

print()
print(f"                       Honest Peter's Garage")
print(f"                         123 Fixit Street")
print(f"                      St. John's, NL A1A 1A1")
print(f"  InvoiceNum: {InvoiceNum:<4s}                                      Date: {DateProcessed:<8s}")
print(f"  --------------------------------------------------------------------")     
print(f"   Customer: {Customer:<30s}     Plate Number: {PlateNum:<6s}")    
print(f"   Address:  {Address:<30s}     Mileage:      {Mileage:<6d}")
print(f"             {City:<30s}")  
print(f"")

LaborDsp = "${:,.2f}".format(CostLabor)
print(f"                                            Cost of Labor:  {LaborDsp:>9s}") 
PartsDsp = "${:,.2f}".format(CostParts)
print(f"                                            Cost of Parts:  {PartsDsp:>9s}") 
DiscountDsp = "${:,.2f}".format(TotalDiscount)
print(f"                                           Total Discount:  {DiscountDsp:>9s}")
HSTDsp = "${:,.2f}".format(HST)
print(f"                                                      HST:  {HSTDsp:>9s}")
print("                                                            ---------")
InvoiceDsp = "${:,.2f}".format(InvoiceTotal)
print(f"                                            Invoice Total:  {InvoiceDsp:>9s}")
print(f"  -------------------------------------------------------------------") 
print(f"      Honest Peter's - There to meet the needs of our customer!!")
print(f"  -------------------------------------------------------------------")                        
