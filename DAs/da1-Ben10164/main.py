##############################################
# Programmer: Ben Puryear
# Class: CptS 222-01, Fall 2021
# Data Assignment #1
# 9/15/21
# I attempted the bonus...
#
# Description: This program computes the mean, median, standard deviation, largest, and smallest number, as well as the amount of numbers in a data set
##############################################
import math

# making the list
number_list = [84.4, 75.8, 42.1, 25.9, 51.1, 40.5, 78.4, 30.3,
               47.7, 58.3, 90.8, 50.5, 28.2, 75.6, 61.8, 25.1, 91.0]
print("The list of numbers is:", number_list)

# Count of the numbers
number_list_count = len(number_list)

# Mean
number_list_total = 0  # This will be the sum of all of the numbers, used for mean
for i in range(number_list_count):
    # Adding up all the numbers in order to calculate mean
    number_list_total += number_list[i]
# Finalizes the calculation of the mean
number_list_mean = number_list_total / number_list_count
# This will be the sum of all of the squared results when subtracting the mean, used in standard deviation
number_list_sqr_nums_total = 0

# Standard Deviation
for i in range(number_list_count):
    # Calculate the sum of all of the squared results when subtracting the mean
    number_list_sqr_nums_total += math.pow(
        (number_list[i] - number_list_mean), 2)
# Calculates the mean of all of the squared results when subtracting the mean
number_list_sqrt_nums_mean = number_list_sqr_nums_total / number_list_count
# Used the mean calculated above to calculate the standard deviation
number_list_standard_deviation = math.sqrt(number_list_sqrt_nums_mean)

# Median Number
number_list_median = 0
sorted_number_list = [84.4, 75.8, 42.1, 25.9, 51.1, 40.5, 78.4, 30.3,
                      47.7, 58.3, 90.8, 50.5, 28.2, 75.6, 61.8, 25.1, 91.0]  # Creates a new array. This array will be sorted
sorted_number_list.sort()  # This is a built in function that sorts a list
print("sorted is ", sorted_number_list)
if len(sorted_number_list) % 2 == 0:  # If there are an even amount of numbers
    number_list_median = (
        sorted_number_list[number_list_count//2] + sorted_number_list[(number_list_count//2) - 1]) / 2
else:  # If there are an odd amount of numbers
    number_list_median = sorted_number_list[number_list_count // 2]

# Largest Number
number_list_largest = number_list[0]
for i in range(number_list_count):
    if number_list[i] > number_list_largest:  # Finding the largest number
        number_list_largest = number_list[i]

#     Smallest Number
number_list_smallest = number_list[0]
for i in range(number_list_count):
    if number_list[i] < number_list_smallest:  # Finding the smallest number
        number_list_smallest = number_list[i]

print("The total amount of numbers are:", number_list_count)
print("The average of the numbers is:", round(number_list_mean, 2))
print("The standard deviation of the numbers is:",
      round(number_list_standard_deviation, 2))
print("The median number is:", round(number_list_median, 2))
print("The smallest number is:", number_list_smallest)
print("The largest number is:", number_list_largest)


# User altered list
user_number_list = [84.4, 75.8, 42.1, 25.9, 51.1, 40.5, 78.4, 30.3,
                    47.7, 58.3, 90.8, 50.5, 28.2, 75.6, 61.8, 25.1, 91.0]
# Get the users starting index
print("Please input a starting index:", end=" ")
user_start = input()
if (int(user_start) < 0) | (int(user_start) >= number_list_count):  # Test to see if it is valid
    print("Please restart the program and input a valid starting index")
    quit()

# Get the users stopping index
print("Please input a stopping index:", end=" ")
user_stop = input()
if (int(user_stop) < 0) | (int(user_stop) >= number_list_count) | (int(user_stop) < int(user_start)):  # Test to see if it is valid
    print("Please restart the program and input a valid stopping index")
    quit()

for i in range(int(user_start), int(user_stop) + 1):
    user_number_list[i] = 0

# Output the altered list
print("The user altered list is:", user_number_list)


# Bonus
print("The original array in reverse being seperated by \" _ \" is:")
for i in range(1, number_list_count+1):
    # I hope it is okay that the last number still has a " _ " after it
    print(number_list[-i], end=" _ ")
