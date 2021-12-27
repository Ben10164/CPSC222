import math

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
