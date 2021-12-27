##############################################
# Programmer: Ben Puryear
# Class: CptS 222-01, Fall 2021
# Data Assignment #2
# 9/28/21
# I did not attempt the bonus...
#
# Description: This program computes the mean, median, standard deviation, largest, and smallest number, of any given csv file, with output formating as well
##############################################

# code that defines the utility functions
import math


def clean_lines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()  # override because strings are imunable
    return lines


def remove_whitespaces(data):
    for line in data:
        for i in range(len(line)):
            line[i] = line[i].strip()


def convert_column_to_numeric(data):
    for i in range(len(data)):
        data[i] = float(data[i])


def read_data(filename):
    # opens filename for reading and loads the column names into a 1D list called headers
    # and loads the data into a 2D list called data
    # returns headers AND data

    infile = open(filename, "r")
    lines = infile.readlines()
    cleaned_lines = clean_lines(lines)

    data = []  # going to be a 2d list
    for line in cleaned_lines:
        values = line.split(",")
        # print(values)
        data.append(values)

    headers = data.pop(0)  # get rid of the headers while assigning

    return headers, data


def display_table(headers, data):
    # displays the header row and the data in a grid-like table format

    joined_list = data.copy()
    # add headers to joined_list acting as a single index (keeping all of joined_list 2d)
    joined_list.insert(0, headers)

    for line in joined_list:
        for obj in line:
            # the space before the tab is beacuse since  a few of the dates are 8 chars, and other are 9, the tabing is different
            print(obj, '', end=' \t')
        print()


def get_column(headers, col_name, data):
    # returns a 1D list representing the column named col_name in data
    formated_col_name = col_name.lower()
    index = -1
    for i in range(len(headers)):
        if headers[i].lower() == formated_col_name:
            index = i
    if index == -1:  # must not be a correct spelling
        return -1

    col = []
    for i in range(1, len(data)):
        col.append(data[i][index])
    if col[1].isdigit():
        new_col = []
        for obj in col:
            new_col.append(float(obj))
        return new_col
    return col

# mean
# median
# standard dev
# min
# max


# Mean
def calculate_mean(data):  # util.calculate_mean(data[1])
    data_total = 0  # This will be the sum of all of the numbers, used for mean
    for i in range(len(data)):
        # Adding up all the numbers in order to calculate mean
        data_total += data[i]
    # Finalizes the calculation of the mean
    number_list_mean = data_total / len(data)
    # This will be the sum of all of the squared results when subtracting the mean, used in standard deviation
    return number_list_mean


# Standard Deviation
def calculate_standard_dev(data):
    data_mean = calculate_mean(data)
    for i in range(len(data)):
        data_sqrt_total = 0
        # Calculate the sum of all of the squared results when subtracting the mean
        data_sqrt_total += math.pow(
            (data[i] - data_mean), 2)
    # Calculates the mean of all of the squared results when subtracting the mean
    number_list_sqrt_nums_mean = data_sqrt_total / len(data)
    # Used the mean calculated above to calculate the standard deviation
    data_standard_dev = math.sqrt(number_list_sqrt_nums_mean)
    return data_standard_dev


# Median Number
def calculate_median(data):
    sorted_data = data.copy()
    sorted_data.sort()  # This is a built in function that sorts a list
    if len(sorted_data) % 2 == 0:  # If there are an even amount of numbers
        number_list_median = (
            sorted_data[len(sorted_data)//2] + sorted_data[(len(sorted_data)//2) - 1]) / 2
    else:  # If there are an odd amount of numbers
        number_list_median = sorted_data[len(sorted_data) // 2]
    return number_list_median


# Largest Number
def find_largest(data):
    data_largest = data[0]
    for i in range(len(data)):
        if data[i] > data_largest:  # Finding the largest number
            data_largest = data[i]
    return data_largest


# Smallest Number
def find_smallest(data):
    data_smallest = data[0]
    for i in range(len(data)):
        if data[i] < data_smallest:  # Finding the largest number
            data_smallest = data[i]
    return data_smallest


# All of the stats
def calculate_stats(headers, name, data):
    data_column = get_column(headers, name, data)
    convert_column_to_numeric(data_column)
    return find_smallest(data_column), find_largest(data_column), calculate_mean(data_column), calculate_median(data_column), calculate_standard_dev(data_column)
