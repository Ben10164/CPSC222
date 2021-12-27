import utils


# promts the user for a coumn name to compute the stats for
headers, data = utils.read_data("export.csv")
#utils.display_table(headers, data)

utils.display_table(headers, data)

user_input = input(
    "Please enter a column to see the stats for!\nOptions: \"Distance walking / running(mi)\" \"Flights climbed(count)\" \"Step count(count)\"\n")
min, max, mean, median, standard_dev = utils.calculate_stats(
    headers, "step count(count)", data)
print("Min: ", "{:.2f}".format(min))
print("Max: ", "{:.2f}".format(max))
print("Mean: ", "{:.2f}".format(mean))
print("Meadian ", "{:.2f}".format(median))
print("Standard Deviation: ", "{:.2f}".format(standard_dev))
