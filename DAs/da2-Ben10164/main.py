##############################################
# Programmer: Ben Puryear
# Class: CptS 222-01, Fall 2021
# Data Assignment #2
# 9/28/21
# I did not attempt the bonus...
#
# Description: This program computes the mean, median, standard deviation, largest, and smallest number, of any given csv file, with output formating as well
##############################################

# code that calls the utility functions
import utils


def main():
    # promts the user for a coumn name to compute the stats for
    headers, data = utils.read_data("fitbit_data_3-8_9-16.csv")
    utils.display_table(headers, data)
    col = -1
    while col == -1:  # just a fun way i implemented repetition until a valid column is inputed
        user_input = input(
            "What column of data would you like the stats to be displayed? ")
        col = utils.get_column(headers, user_input, data)
        if col == -1:
            print("Sorry but you must have spelled something wrong")
            print("Please try again")
        else:
            min, max, mean, median, standard_dev = utils.calculate_stats(
                headers, user_input, data)
            print("Min: ", "{:.2f}".format(min))
            print("Max: ", "{:.2f}".format(max))
            print("Mean: ", "{:.2f}".format(mean))
            print("Meadian ", "{:.2f}".format(median))
            print("Standard Deviation: ", "{:.2f}".format(standard_dev))


main()
