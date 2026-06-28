# tech-basic

PythonとWebアプリ開発の基礎を体系的に学び、日本ETFのペーパートレード管理アプリとして成果物化するための個人開発プロジェクトです。

Pythonの基本文法から、CSV、JSON、pandas、SQLite、FastAPI、pytest、Git/GitHubまで段階的に学習し、Day 29ではETFの価格、売買シグナル、損益をWeb画面に表示しました。

Codexは完成コードを丸ごと作らせるためではなく、学習コーチ、レビュー担当、進捗管理の補助として使い、自分で実装して動作確認する流れを重視しています。

## 目的

就活・研究・個人開発で説明できる実装力を身につけることを目的としています。

このリポジトリでは、1つの大きな完成アプリを最初から作るのではなく、Dayごとに小さなテーマを実装し、最後に日本ETFペーパートレード管理アプリとして説明できる形にまとめています。

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
- ETFの価格、売買シグナル、損益を表示するWeb画面

## リポジトリ構成

```text
dayX.py        各Dayの学習コード
notes/         各Dayの学習記録
test_dayXX.py  pytest用のテストコード
AGENTS.md      学習ロードマップと進捗管理
```

各Dayのファイルは、1つの完成アプリではなく、学習内容ごとに独立しています。

Day 29の `day29.py` では、これまで学んだ関数、条件分岐、FastAPI、HTML表示を組み合わせて、ETF管理アプリの画面を作成しています。

## Codexの活用方針

このリポジトリでは、Codexを単なるコード生成ツールとして使うのではなく、学習の進め方を守るためのコーチとして活用しています。

- `AGENTS.md` に学習方針、進め方、進捗を記録する
- 完成コードを最初から出さず、小さい例とヒントをもとに自分で実装する
- 実行結果やエラーを確認してから、原因整理や改善点のレビューを受ける
- 各Dayの最後に `notes/dayX.md` とGit commitで学習履歴を残す

## 実行方法

通常のPythonファイルは、確認したいDayのファイルを指定して実行します。

```powershell
python day1.py
python day12.py
```

FastAPIを使うDayは、uvicornで起動します。

```powershell
uvicorn day20:app --reload
uvicorn day29:app --reload
```

pytestのテストは、次のコマンドで実行します。

```powershell
python -m pytest
```

## Day 30で整理したこと

これまで学んだPython、SQLite、FastAPI、HTML、pytest、Git/GitHubを、就活用に説明しやすい成果物として整理しました。
