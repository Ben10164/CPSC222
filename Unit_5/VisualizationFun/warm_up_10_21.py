import matplotlib.pyplot as plt
import pandas as pd

msrp_df = pd.read_csv("msrp.csv")

new_row = pd.Series(["chevy corvette", 77, 2212],
                    index=["CarName", "ModelYear", "MSRP"])

# ignore index means there is no name for this series, auto increment in a way, instead of trying to sort it
msrp_df = msrp_df.append(new_row, ignore_index=True)

print(msrp_df)

counts_ser = msrp_df["ModelYear"].value_counts()
print(counts_ser)

ModelYearSplit = msrp_df.groupby("ModelYear")
meanStuff = ModelYearSplit["MSRP"].mean()
print(meanStuff)
