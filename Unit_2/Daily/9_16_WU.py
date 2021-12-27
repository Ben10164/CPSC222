import math

help(print)

# Functions
# the body of the functions only runs when you call the function
# Ex 1, no parameter, no output


def say_hello():
    print("Hello")


say_hello()

# Ex 2, one parameter, no output


def say(message):
    print(message)


say("Hi There!")

# Ex 3, one parameter, one return


def compute_circle_area(radius):
    area = math.pi * radius ** 2
    return area


result = compute_circle_area(10)
print(result)

# Ex 4 one parameter, two return values


def compute_circle_area_and_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


result1, returlt2 = compute_circle_area_and_circumference(5.0)
