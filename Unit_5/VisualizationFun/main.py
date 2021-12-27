# EDA: exploratory data analysis
# getting familiar with your data
# visualizing data, minning data (looking for groups, patterns, etc)

# goals of data vis
# 1. clearly and accuratley represent data
# 2. be creative, with the goal of increasing readability and understanding
# 3. label the units, and points of interest

# jargon
# chart: a 2D visualization
# plot: a chart wth data points (e.g. scatter plot)
# graph: chart for a math function (e.g. sine)

# we will use the matplotlib libary for charting w/ python
# 3 ways to use matplotlib
# 1. using the pyplot module (what data scientits typically use)
#   *there is always a "current" figure*
import matplotlib.pyplot as plt
# 2. using the OOP interface
# 3. mix of the first two


import numpy as np

# a simple line chart


def line_chart_example(x, y, y2, filename):
    # x and y would be
    # 1D list, numpy arrays, pandas series, etc.
    plt.plot(x, y, label="x Squared")
    plt.plot(x, y2, color="red", lw=2, label="x Cubed")

    plt.legend()
    plt.grid()
    plt.title("Our First Chart in 222")
    plt.xlabel("X Units")
    plt.ylabel("Y Units")

    # now we need to show the plot

    # 3 main ways
    # 1. plt.show(): opens a window
    # plt.show()
    # 2. plt.savefig(filename): saves to a file
    plt.savefig(filename)
    # 3. inline with jupyter notebook


def scatter_chart_example(x, y, filename):
    plt.figure()  # creates a new "current" figure
    plt.scatter(x, y, color="green", marker='x', s=500)
    plt.savefig(filename)


def bar_chart_example(x, y, filename):
    plt.figure()  # creates a new "current" figure
    plt.bar(x, y, color="red")
    plt.savefig(filename)


def pie_char_example(x, y, filename):
    plt.figure()  # creates a new "current" figure
    plt.pie(y, labels=x, autopct="%1.1f%%")
    plt.savefig(filename)


def histogram_chart_example(data, filename):
    plt.figure()
    # by default there are 10 bins, aka, intervals
    plt.hist(data, bins=30, edgecolor="black")
    plt.savefig(filename)


def main():
    # we need some data
    x = list(range(0, 6))
    y = []  # y will be squares of x
    y2 = []  # z will be cubes of x

    for val in x:
        y.append(val**2)

    for val in x:
        y2.append(val**3)

    line_chart_example(x, y, y2, "line_example.png")

    # this will continue using the current figure
    # if you want to make a new plot then you need to clear the figure
    scatter_chart_example(x, y, "scatter_example.png")

    bar_chart_example(x, y, "bar_example.png")

    pie_char_example(x, y, "pie_example.png")

    # randomly select 1000 points from a normal distrobution
    # with mean 100 and stdv of 20

    np.random.seed(0)  # seed(0) for reproducivity
    mean = 100
    stdv = 20
    num_samples = 100
    random_data = np.random.normal(mean, stdv, num_samples)

    histogram_chart_example(random_data, "histograph_example.png")


main()
