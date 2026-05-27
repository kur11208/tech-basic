# Day 10: JSON read/write
import json

data = {
    "TOPIX": 2000,
    "日経225": 30000,
}

with open("etf_prices.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)

with open("etf_prices.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

for name in loaded_data:
    print(name + ": " + str(loaded_data[name]))
