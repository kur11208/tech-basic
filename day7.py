# Day 7: 例外処理・ログ

# 今日の練習:
# ETF価格を入力して、数字に変換できない場合はエラーメッセージを表示します。

# ここから下に、自分でコードを書いてみましょう。
import logging
logging.basicConfig(filename="day7.log", level=logging.INFO)
number = input("価格を入力してください:")
try:
    number = int(number)
    print("価格:", number)
    logging.info("価格の入力に成功しました")
except ValueError:
    print("数字で入力してください")
    logging.info("数字ではない入力がありました") 