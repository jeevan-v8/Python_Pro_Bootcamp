print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
finaltip = bill*(tip/100)
split = (bill + finaltip)/people
finalbill = round(split,2)
print(f"Each person should pay: {finalbill}")
