# Day 13 学習記録

## 今日やったこと

- FastAPIを使って、ブラウザに文字を表示する小さいWebアプリを作った
- `uvicorn` を使ってFastAPIアプリを起動した
- ブラウザで `/` にアクセスして表示を確認した
- 存在しないURLにアクセスしたときの `Not Found` を確認した

## 今日わかったこと

- FastAPIアプリは `python day13.py` ではなく、`uvicorn` で起動する
- `FastAPI()` はWebアプリ本体を作るために使う
- `@app.get("/")` は `/` にGETアクセスされたときに動く処理を指定する
- `day13:app` は `day13.py` の中の `app` を起動するという意味

## 詰まったところ

- FastAPIアプリは `python day13.py` ではなく、`uvicorn` で起動するところ

## 自分の言葉で説明

- FastAPIは、ブラウザからアクセスされたときに何を返すかをPythonで書けるWebアプリの道具

## 次回やること

- GETとPOSTの違いを学ぶ
