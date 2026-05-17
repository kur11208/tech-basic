# Day 6: 関数

# ここに、ETF名と価格を受け取って表示する関数を書いてみましょう。
def show_etf_info(name,price):
      print("ETF名:", name)
      print("価格:", price)

show_etf_info("TOPIX",2500)
show_etf_info("日経225",38000)
def calculate_value(price,count):
    return price*count
print("評価額:", calculate_value(2500,3))
print("評価額:", calculate_value(1000,1))
print("評価額:", calculate_value(2500,0))