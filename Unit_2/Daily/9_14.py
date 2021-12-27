import math
import random

x = 0
if x == 6:
    print("x is 6")
else:
    print("x is NOT 6")

# elif
# use elif if you want to test multiple conditions
# in order. The first one that is true will run
x = -5
if x < 0:
    print("x is a negative number")
elif x > 0:
    print("x is a positive number")
else:  # this else at the end is only if all other are false (like a catch)
    print("x is zero")

# loops
# for loops
# for item in sequence:
    # statements to be repeated

# lists are sequences
my_list = [1, 6, 3, 8]
for val in my_list:
    print(val, end=" ")
print()

# strings are sequences
my_string = "Hello!"
for char in my_string:
    print(char, end=" ")
print()

# range(n) -> [0,n)
# range(n, m) -> [n,m)
# range(n,m,p) ->[n,m) increasing by step
for i in range(3):
    print(i, end=" ")  # prints from 0 to 2
print()

for i in range(1, 3):
    print(i, end=" ")  # prints from 1 to 2
print()

for i in range(1, 7, 2):
    print(i, end=" ")  # odd numbers between [1,7), increasing by 2
    # 1 3 5
print()

for i in range(5, -10, -2):
    print(i)

# while loop
k = 1
while k < 10:
    print(k, end=" ")
    k += 2
print()

# while True:
#     user_input = input("enter a word (stop to quit): ")
#     if user_input == "stop":
#         break

# random numbers
die_roll1 = random.randrange(1, 7)  # [1,7)
print("Die roll 1: ", die_roll1)
die_roll2 = random.randint(1, 6)  # [1,6]
print("Die roll 2: ", die_roll2)

# you can also seed the generator with a constant
random.seed(0)
print(random.randint(1, 6))
