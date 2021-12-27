import pandas as pd
from pandas.core import groupby


header = ["City", "Population", "Class"]

data = [["Spokane", 219190, "Medium"], ["Seattle", 944955, "Large"], [
    "Bellevue", 147599, "Medium"], ["Leavenworth", 2010, "Small"]]

pop_df = pd.DataFrame(data, columns=header)

# our index is our key (uniquely defines the row)
# we can also use the city column as the index
pop_df = pop_df.set_index("City")


# index/sclicing
# grab a column by its label (returns a series)
# a single column is a series

pop_ser = pop_df["Population"]  # Gives column 0

pop_ser = pop_df.iloc[0]  # gives row 0


pop_spokane = pop_df.iloc[0, 0]


# you can also use loc for label based indexing
pop_spokane = pop_df.loc["Spokane", "Population"]


# slice across colums with more than one column returns a dataframe

# really cool parts

# lets open regions.csv and store the data in a dataframe
regions_df = pd.read_csv("regions.csv", index_col=0)


# lets join pop_df and regions_df on the attribute
# that they both share (city)
# left.merge(right,on="Index to merge on")
merged_df = pop_df.merge(regions_df, on="City")  # inner join by default
print(merged_df)

# we can write dataframes (and series) to files
merged_df.to_csv("merged.csv")

# data aggregation: gathering and summarizing data
# split-apply-combine
# 1 split on the class attructe
# use pandas groupby() to do this

grouped_by_class = merged_df.groupby("Class")
print(grouped_by_class.groups.keys())
medium_df = grouped_by_class.get_group("Medium")
print(medium_df)

# we want to write general code to process each group
# no matter how many groups there are
# apply
# apply mean to the population column
mean_pop_ser = pd.Series(dtype=float)
for group_name, group_df in grouped_by_class:
    print(group_name)
    print(group_df)
    group_pop_ser = group_df["Population"]
    mean_group_pop = group_pop_ser.mean()
    print(mean_group_pop)
    # step 3
    # combine ( we want to combine the means of each class into a single Series)
    mean_pop_ser[group_name] = mean_group_pop

    print("***********")

print(mean_pop_ser)


# or just one line
mean_pop_ser = grouped_by_class["Population"].mean()
print(mean_pop_ser)
