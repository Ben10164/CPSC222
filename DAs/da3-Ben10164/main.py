import pandas as pd

# reads the youtube analytics to a dataframe
youtube_df = pd.read_csv(
    "youtube_analytics_9-20-20_9-20-21.csv", index_col="Date")

# reads the days of week file to a dataframe
days_df = pd.read_csv("days_of_week_9-20-20_9-20-21.csv", index_col="Date")

# gets the users input for the start and end date
slice_start_date = input("What date you like the slice to start? ")

slice_end_date = input("What date you like the slice to end? ")

# creates a new dataframe that is youtube_df sliced based on the user inputs
sliced_youtube_df = youtube_df.loc[slice_start_date: slice_end_date]

# displays the available options (the keys)
print("The options for a collumn to calculate stats for are, ",
      sliced_youtube_df.keys())


# getting the user specific column
user_specified_col = input(
    "Which column would you like to view the stats of? ")


# slicing by the column the user specifies
sliced_youtube_s = sliced_youtube_df[user_specified_col]

# uses pandas to calculate all the stats (we love pandas)
sliced_youtube_stats_s = pd.Series(dtype=float)
sliced_youtube_stats_s["Sum"] = sliced_youtube_s.sum()
sliced_youtube_stats_s["Mean"] = sliced_youtube_s.mean()
sliced_youtube_stats_s["StdDev"] = sliced_youtube_s.std()
sliced_youtube_stats_s["Median"] = sliced_youtube_s.median()
sliced_youtube_stats_s["Smallest"] = sliced_youtube_s.min()
sliced_youtube_stats_s["Largest"] = sliced_youtube_s.max()

# outputs to a file called 'user_specified_timespan_stats.csv'
sliced_youtube_stats_s.to_csv(
    "user_specified_timespan_stats.csv", header=False)

# PART 2

merged_df = youtube_df.join(days_df, on="Date")
merged_df.to_csv("merged.csv")


# split
merged_day_df = merged_df.groupby("Day of Week")

# apply AND combine
# making a new series that is the mean of each of the rows in the user specified column
merged_user_col_mean_s = merged_day_df[user_specified_col].mean()

# outputing to a csv
merged_user_col_mean_s.to_csv("merged_user_specified_col_mean.csv")
