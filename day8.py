# Day 8: テキストファイル読み書き

# ETFメモを書き込み、読み込んで表示する
with open("etf_memo.txt", "w", encoding="utf-8") as file:
    file.write("TOPIXを確認する\n日経225を確認する")
with open("etf_memo.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)
