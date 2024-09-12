# This lesson we entered values into our inputs, that were already given to us
# For output(values displayed), we still use 'f string' format
# Remember to use int,float, or "" depending on value or name

# Gathering my inputs 
Team = "St. John's Pebbles Football Team "
Program = "Game Statistics Program"
Values = "Please enter the following required values: "
Date = "      Game Date (yyyy-mm-dd): "
Opponent = "      Opponent: "

NumPassAtt = 46 # int(input("The Number of pass attempts: "))
NumComp = 25 # int(input("The number of completions: "))
TotPassYards = 425 # int(input("Total passing yards: "))
NumTD = 2 # int(input("The number of touchdowns: "))
NumInt = 0 # int(input("Number of interceptions: "))

NumRushAtt = 10 # int(input("The number of rushing attempts: "))
TotRushYards = 75 # int(input("Total Rushing Yards: "))
NumRushTd = 2 # int(input("Rushing touchdowns: "))

# Quarterback Calculations 
PassPercent = (NumComp) / (NumPassAtt)
YardsPP = (NumComp / TotPassYards) * 100
FormOne = (PassPercent - 0.3) * 5
FormTwo = (TotPassYards / NumPassAtt - 3) * 0.25
FormThree = (NumTD / NumPassAtt) * 20 
FormFour = 2.375 - ((NumInt / NumPassAtt) * 25)
NFLPassRate = ((FormOne + FormTwo + FormThree + FormFour) / 6) * 100

# Rushing Calculations
AvgYards = (TotRushYards) / (NumRushAtt)
TDEff = (NumRushTd) / (NumRushAtt)

# Display my results
print()
print("St. John's Pebbles Football Team")
print("Game Statistics Program")
print()
print("Game Statistics:            Kansas City Chiefs vs Buffalo Bills ")
print("---------------------------------------------------------------")
# Quarterback part
print("Quarterback Statistics: Patrick Mahomes ")
print("")
PassCompDsp = "{:.0%}".format(PassPercent)
print(f"Number of pass attempts:  {NumPassAtt:>2d}   Pass Completions %:          {PassCompDsp:>4s}")
print(f"Number of completions:    {NumComp:>2d}")
YardsPassDsp = "{:.0f}".format(YardsPP)
print(f"Total passing yards:     {TotPassYards:>3d}   Yards per Pass:               {YardsPassDsp:>3s}")
print(f"Number of touchdowns:      {NumTD:>1d}")
NFLDsp = "{:.1f}".format(NFLPassRate)
print(f"Number of interceptions:   {NumInt:>1d}   NFL Passer Rating:          {NFLDsp:>5s}")
print()
# Rushing Part
print("Rushing Statistics: Isaiah Pacheco ")
print()
YardsRushDsp = "{:.1f}".format(AvgYards)
print(f"Number of rushing atts:  {NumRushAtt:>2d}    Avg Yards Per Rush:          {YardsRushDsp:>4s}")
print(f"Total Rushing Yards:    {TotRushYards:>3d}")
TDEffDsp = "{:.0%}".format(TDEff)
print(f"Number of rushing TD's:   {NumRushTd:>1d}    TD Efficiency:              {TDEffDsp:>5s}")
print(f"----------------------------------------------------------------")
