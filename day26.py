import pandas as pd

# etf_prices.csv を読み込み、ETF名の列を表示するコードを書いてください。
df = pd.read_csv("etf_prices.csv")
print(df["ETF名"])
print(df["価格"])
