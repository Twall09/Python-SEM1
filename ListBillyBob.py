# Lesson 25-26, LIST EXAMPLES 

# Billy Bob number cruncher program

NumLst = []
while True:
    Number = input("Enter a number (-1 to end): ")
    Number = int(Number)
    if Number == -1:
        break

    NumLst.append(Number)

print()
print("Horizontal List:")
print(NumLst)

# OR

print()
print("Vertical List:")
NumIndex = 0
for Number in NumLst:
    print()
    print(Number)
    NumIndex += 1

# Sort the list and display (Lowest to highest #)
print()
print("Sorted List:")
NumLst.sort()
print(NumLst)

# Sort in descending order (Opposite)
print()
print("Reverse Order:")
NumLst.sort(reverse = True)
print(NumLst)

# Total of all numbers
print()
print("Sum of all:")
Total = sum(NumLst)
print(Total)

# To count the numbers in a list
print()
print("Number of digits:")
NumNumbers = len(NumLst)
print(NumNumbers)

# Find the average
print()
print("Average:")
Average = Total / NumNumbers
print(Average)

# Find the Minimum and Maximum values in a list
print()
print("Min Value:")
MinValue = min(NumLst)
print(MinValue)
print("Max Value:")
MaxValue = max(NumLst)
print(MaxValue)

# Find the duplicate values in a list
print()
Dups = []
print("Duplicates:")
for Number in NumLst:
    if NumLst.count(Number) > 1 and Dups.count(Number) == 0:
        Dups.append(Number)

Dups.sort()
print(Dups)

