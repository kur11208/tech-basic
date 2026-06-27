# Day 29 学習記録

## 今日やったこと

- FastAPIでHTML画面を表示した
- ETF名、価格、売買シグナル、損益を1画面に表示した
- `get_signal(price)` を使って価格から売買シグナルを作った
- `calculate_profit(buy_price, price, quantity)` を使って損益を計算した
- ブラウザで画面表示を確認した

## 詰まったところ

- HTML文字列の中に余計な `f"` が入ってしまった
- `if` / `elif` / `else` のインデントをそろえる必要があった
- 関数定義の最後に `:` が必要だった
- 使っていない変数名 `current_price` ではなく、実際にある `price` を渡す必要があった
