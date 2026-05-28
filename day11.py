# Day 11: datetime

# ここに、今日の日付と現在時刻を表示するコードを書きます。
from datetime import datetime

time = datetime.now()
trade_date = time.strftime("%Y-%m-%d")
trade_time = time.strftime("%H:%M")
print("ETF取引日:", trade_date)
print("記録時刻:", trade_time)
