# if else condition statements 

print("welcome to Roller-Coster")
height = int(input("Enter your height in cm : \n"))

if height>=120:
   print("you can ride the Roller-Coster")
   age =  int(input("Enter your age : \n"))
   if age < 12:
      print("you have to pay $5")
   elif age>=12 and age<=18:
       print("your have to pay $7")
   else:
      print("you gave to pay $12")
else:
   print("you can't ride the Roller-Coster")


#modulus operator usage with exmple of finding out even or number

#num = int(input("Enter a number : \n"))

#if num%2==0:
#	print("The entered number is even")
#else:
#	print("The entered number is odd")
