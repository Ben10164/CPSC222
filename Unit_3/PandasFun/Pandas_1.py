import pandas as pd

"""
pandas is showrt for panel data
it is a lbrary, like numpy, for data science
it is built on numpy

there are two main objects in pandas
1D data: pandas Series
2D data: pandas DataFrame(every column is a series)
"""

# Series
# there are a few ways to make a series

populations = [219190, 944955, 147599, 2010]  # These are parallel lists
cities = ["Spokane", "Seattle", "Bellevue", "Leavenworth"]

pop_ser = pd.Series(populations)
print(pop_ser)


# this is saying that the inde label is the populations list
pop_ser = pd.Series(populations, index=cities)
pop_ser.name = "Population"
print(pop_ser)  # notice how it also outputs the name, not just the dtype

print(pop_ser["Seattle"])
print(pop_ser[["Seattle", "Leavenworth"]])  # you can use a list as an index
print(pop_ser["Seattle": "Leavenworth"])  # NOTICE HOW THIS INCLUDES THE STOP

# is also good since it still supports order based indexing

# use .iloc[] (Index Location)
print(pop_ser.iloc[1])
print(pop_ser.iloc[[1, 3]])
print(pop_ser[1:3])  # OK THIS DOESNT INCLUDE THE STOP
# Pandas support label based indexing
# we can name a series
# this is nice if we add the series to a column to a DataFrame

# SUMMARY STATS
# pandas has these (nice)
print(pop_ser.mean())
print(pop_ser.std())

# can add new data to a series
pop_ser["Pullman"] = 34019
print(pop_ser)

# we can create an empty series
pop_ser2 = pd.Series(dtype=int)
pop_ser2["Pullman"] = 34019
print(pop_ser2)


# data frame
# data frames are used to store 2d data in pandas
twod_list = [[3, "a", 4.5], [7, "b", 10.99], [-10, "c", -1.5]]
header = ["col1", "col2", "col3"]
df = pd.DataFrame(twod_list)  # df is short for dataframe
print(df)

df = pd.DataFrame(twod_list, columns=header)
print(df)
# the column labels are called 'colums'
# the row labels are called 'index'
# rows also support label based indexing

row_index = ["row1", "row2", "row3"]
df = pd.DataFrame(twod_list, columns=header, index=row_index)
print(df)

# task: create pop_df
# dataframe for the population data
# 3 columns
# spokane, seattle, bellevue, leavenworth
# 219190, 944955, 147599, 2010
# medium, large, medium, small

