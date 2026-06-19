# tech-basic

PythonとWebアプリ開発の基礎を学ぶためのリポジトリです。

Dayごとに独立した小さなプログラムを作成し、最終的に日本ETFペーパートレード管理アプリを作ることを目標にしています。

## 目的

PythonとWebアプリ開発のスキルアップを目的としています。

## 身につけた技術

- Pythonの基本文法
  - 変数、型、条件分岐、繰り返し、list、dict、関数を使った処理を書ける
- 例外処理とログ
  - 入力ミスなどでエラーが起きる場合に、プログラムを止めずに処理できる
  - loggingを使って処理の記録をファイルに残せる
- ファイル操作
  - テキストファイル、CSV、JSONを読み書きできる
- pandas
  - CSVをDataFrameとして読み込み、列や先頭行を確認できる
- SQLite
  - PythonからSQLiteに接続できる
  - INSERT / SELECT / UPDATE / DELETE を使ってデータを追加、取得、変更、削除できる
- FastAPI
  - GET / POST のAPIを作成できる
  - HTMLを返してWeb画面を表示できる
  - SQLiteのデータをAPIとして返せる
- pytest
  - assertを使って関数の結果を確認できる
  - FastAPIのTestClientを使ってAPIの動作確認ができる
- Git / GitHub
  - git status、git add、git commitで学習履歴を管理できる
  - remoteを設定し、GitHubへpushして公開できる

## 作成したもの

- Pythonの基本文法を確認する小さなプログラム
- CSV、JSON、SQLiteを使ったデータ保存と読み込みの練習
- FastAPIを使ったAPIとHTML表示の練習
- pytestを使った自動テスト
- GitHub公開までの学習記録

## リポジトリ構成

```text
dayX.py        各Dayの学習コード
notes/         各Dayの学習記録
test_dayXX.py  pytest用のテストコード
AGENTS.md      学習ロードマップと進捗管理
```

各Dayのファイルは、1つの完成アプリではなく、学習内容ごとに独立しています。

## 実行方法

通常のPythonファイルは、確認したいDayのファイルを指定して実行します。

```powershell
python day1.py
python day12.py
```

FastAPIを使うDayは、uvicornで起動します。

```powershell
uvicorn day20:app --reload
```

pytestのテストは、次のコマンドで実行します。

```powershell
python -m pytest
```

## 今後の予定

Day 30までに、これまで学んだPython、SQLite、FastAPI、HTML、pytest、Git/GitHubを組み合わせて、日本ETFペーパートレード管理アプリとしてまとめる予定です。
