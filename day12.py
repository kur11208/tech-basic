# Day 12: pandas

# TODO:
# 1. import pandas as pd
# 2. read etf_prices.csv into df
# 3. print df
import pandas as pd
df = pd.read_csv("etf_prices.csv")
print(df)
print(df["価格"])
print(df.head(2))