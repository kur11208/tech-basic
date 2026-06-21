def get_signal(price):
    # ここに、価格に応じて「買い」「売り」「様子見」を返す処理を書く
    if price<1000:
        return "買い"
    elif price >1500:
        return "売り"
    else:
        return "様子見"
print(get_signal(900))
print(get_signal(1000))
print(get_signal(1600))


# 関数ができたら、ここで価格を渡して結果を表示する
