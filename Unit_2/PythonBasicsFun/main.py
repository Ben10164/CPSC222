import math
# this is a comment
# a line of code that is ignored by python when it runs the program
# we use comments to document our code

'''
these are triple quotes
everything in between these are commented
this is a comment block
'''

'''
print(5 / 2)
print(5 // 2)

x = 5  # x is assigned to 5, not x equals 5
print(x)
print(type((x)))
# a variable stores a value
# a value has a 'data type' which defines the range of values
x = 5.5
print(x)
print(type((x)))
x = "hello"
print(x)
print(type((x)))
print(2 ** 5)  # power - 2^(5)
print(pow(2, 5))  # this is an int
# using the math library
print(math.pow(2, 5))  # this is a float
print(math.cos(math.pi))

print("Hello World")

# getting input from the user
print("Enter your favorite number: ")
# favorite_number = input()
favorite_number = 3
print("Your favorite number is: ", favorite_number)

# it is wrong because it is a string
print("Your favorite number doubled incorrectly is: ", favorite_number*2)

# how to convert
favorite_number_int = int(favorite_number)
print("Your favorite number doubled correctly is: ", favorite_number_int * 2)

# this is using keyword arguments (notice the extra arguments)
print("Your favorite number doubled correctly is: ",
    favorite_number_int * 2, sep="", end=":)")
print()


# FORMATTING floating point numbers
print(math.pi)
# C/C++ style
# .3 means 3 points after decimal, f means float
print("%.3f" % (math.pi))
# Python style
# .2f means 2 points after decimal, f means float
print("{:.2f}".format(math.pi))
# Rounding Style
# Unlike the other two, this last approach actually stores the rounded value
print(round(math.pi, 2))
# but you can also do
temp = round(math.pi, 5)
print(temp)


print("Please enter the voltage:")
voltage_string = input()
voltage_int = float(voltage_string)

print("Please enter the resistance:")
resistance_string = input()
resistance_int = float(resistance_string)

print("")
power = (voltage_int ** 2) / resistance_int
print("The power is:")
print("{:.2f}".format(power))
'''
# Conditionals
x = 6
if x == 6:
    print("x is 6")
