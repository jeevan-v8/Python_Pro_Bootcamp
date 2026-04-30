# pizza order practice using if/else conditional statement

print("Welcome to python pizza delivery system -- customise you own pizza")

size = input("What size do you want? S, M and L :")
pepparoni = input("Do you want pepparoni on your pizza? type Y for yes and N for no :")
cheese = input("Do you want extra cheese? Y or N :")

bill = 0

if size == "S":
   bill +=15
elif size == "M":
   bill +=20
elif size == "L":
   bill += 25
else:
   print("wrong inputs")


if pepparoni == "Y":
   if size == "S":
      bill +=2
   else:
      bill += 3

if cheese == "Y":
   bill +=1

print(f"your total bill : {bill}")
