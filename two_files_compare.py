import pandas as pd
import numpy as np

T_df = pd.read_csv("PlayersFull_420.csv")
L_df= pd.read_csv("output.csv")

All_df = pd.merge(T_df,L_df, on=["FirstName","LastName"], how="outer", indicator = True)
print(All_df._merge)
All_df=All_df[All_df['_merge']=='right_only']
print(All_df[["FirstName","LastName"]])
