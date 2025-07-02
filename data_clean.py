import pandas as pd
df= pd.read_csv(r'C:\AI PROJECT\cdd (1)\cdd.csv')
print(df.isnull().sum())
df_clean=(df.dropna())
print(df_clean)
df["V3"]=df["V3"].fillna(df["V3"].mean())
df["V1"]=df["V1"].replace({0:0,1:1})

