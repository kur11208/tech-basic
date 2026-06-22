def calculate_profit(buy_price, current_price, quantity):
    # 購入価格・現在価格・口数から損益を計算して返す
    return (current_price-buy_price)*quantity
profit = calculate_profit(1000, 1100, 10)
print(profit)
profit = calculate_profit(1000, 900, 10)
print(profit)
profit = calculate_profit(1000, 1000, 10)
print(profit)