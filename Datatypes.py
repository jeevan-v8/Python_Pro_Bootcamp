# Datatypes in python

print(type("hello"))
print(type(123))
print(type(3.14))
print(type(True))

# type conversion

print(int("123") + int("456")) # here inside bracket normally it is a string but since we used int - it will treat those as integer

print("Number of letters in your name : " + str(len(input("Enter your name \n")))) 

name = "Jeevan"
length = len(name)
print(type(length))
