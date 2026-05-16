# Day 5: dict

etf = {"name": "日経225", "price": 38000}

print("ETF名:", etf["name"])
print("価格:", etf["price"])

for key in etf:
    print(key, etf[key])
