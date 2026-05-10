# Day 2: 条件分岐の練習

name = input("名前を入力してください: ")
age = int(input("年齢を入力してください: "))
money = int(input("所持金を入力してください: "))
score = int(input("点数を入力してください: "))
print(name + "さんのチェック結果です")

if age < 18:
    print("区分: 未成年")
elif age < 65:
    print("区分: 大人")
else:
    print("区分: シニア")

if money >= 1000:
    print("1000円以上あるので、昼ごはんを買えます")
else:
    print("1000円未満なので、今日は節約しましょう")

if age >= 18 and money >= 2000:
    print("映画に行けます")
else:
    print("映画はまた今度にしましょう")

if score >= 80:
    print("よくできました")
elif score >= 60:
    print("合格です")
else:
    print("不合格です")