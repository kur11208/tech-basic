# Day 9: CSV読み書き

# ここに自分でコードを書いていきます。
import csv

with open("etf_prices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["TOPIX", 2000])
    writer.writerow(["日経225", 30000])
    writer.writerow(["JPX400", 18000])
with open("etf_prices.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0] + "," + row[1])
