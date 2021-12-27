import pandas as pd

cars_pd = pd.read_csv("cars.csv", index_col=0)

grouped_by_ModelYear = cars_pd.groupby("ModelYear")

for group_name, group_df in grouped_by_ModelYear:
    print(group_name)
    print(group_df)

'''
uh oh, i have some noisy and invalid data!
what do i do??

ways to deal with these
look for duplicates when there shouldnt be
look for outliers
  sort and print
  visualizations
      your eyes really like this
smooth out values
  you can use a filter for this
  moving average smoothing

ways to handle missing values
  remove them    ( dropna()  )
      only do this is the missing part is a very
      small percentage

  fill or replace them with valid values!
      be careful with this
      do this by hand
          manually
      use a central tendancy measurement
          mean, median and mode for numeric
                (INTERPOLATE() IN PANDAS GIVES A LINEAR 
                    [ DOESNT WORK IF THE FIRST OR LAST IS NA ])
          most frequet value for cateogrical 
      use machine learnign to make a prediction
          for numeric: REGRESION teqnices
          for categorical: classification techinques
      ignore them and deal with them on a case by case basis
          could result with a bunch of if statements

dropna()
isnull().sum() will tell you the amount of NA
    np.NaN
    
'''
