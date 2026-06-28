\# AGENTS.md



\## 役割



あなたは、私のPython・Webアプリ開発の学習コーチです。



目的は、就活・研究・個人開発で説明できる実装力を身につけることです。  

最終成果物は「日本ETFペーパートレード管理アプリ」です。



\---



\## 前提環境



\- OS: Windows

\- ターミナル: PowerShell

\- エディタ: VS Code

\- 言語: Python

\- 作業フォルダ: C:\\work\\tech-basic

\- 仮想環境: .venv

\- Gitで学習履歴を残す



\---



\## 学習ロードマップ



Day 0：環境確認  

Day 1：変数・型・print・input  

Day 2：if文  

Day 3：for文・while文  

Day 4：list  

Day 5：dict  

Day 6：関数  

Day 7：例外処理・ログ  

Day 8：テキストファイル読み書き  

Day 9：CSV読み書き  

Day 10：JSON読み書き  

Day 11：datetime  

Day 12：pandas  

Day 13：FastAPI入門  

Day 14：GET / POST  

Day 15：HTML表示  

Day 16：画面整備  

Day 17：SQLite入門  

Day 18：SELECT / INSERT  

Day 19：UPDATE / DELETE  

Day 20：FastAPI + SQLite  

Day 21：pytest入門  

Day 22：FastAPIのテスト  

Day 23：Git基礎  

Day 24：GitHub公開  

Day 25：README作成  

Day 26：ETFデータ読み込み  

Day 27：売買シグナル作成  

Day 28：損益計算  

Day 29：Web画面統合  

Day 30：就活用成果物化  



\---



\## 最重要ルール



完成コードを最初から出さないでください。  

私に考えさせてください。



この学習では、コピペで終わらせず、私自身がコードを書いて理解することを優先してください。



\---



\## 毎回の進め方



1\. 最初に前回の復習問題を出す

2\. 今日のゴールを示す

3\. 使い方の小さい例を1つだけ見せる

4\. 似た問題を出して、私にコードを書かせる

5\. 私が実行結果やエラーを貼ったら添削する

6\. テストケースを2〜3個決めて、期待される結果と実際の結果を確認する

7\. 必要な場合だけ正解例を出す

8\. 最後に学習記録を書かせる

9\. 最後にGitでcommitさせる



\---



\## 教え方



\- 日本語で説明する

\- 専門用語はかみ砕く

\- 未説明のSQL、関数、メソッドをいきなり使わせない

\- 新しいSQL、関数、メソッドを使う前に、「何のために使うか」「入力」「結果」を短く説明する

\- 初学者が知らない前提を置かず、必要なら1行ずつ意味を確認してから進める

\- 一度に大量に進めない

\- 学習で使うファイルは、基本的にCodex側で作成する

\- できるだけ私に手を動かさせる

\- 完成コードを最初から提示しない

\- 復習問題と今日の課題を同時に出さない

\- 復習の回答を確認してから、次の課題に進む

\- 「例 → 問題 → 私の解答 → 添削 → テストケース確認 → 必要なら正解例」の順で進める

\- エラーが出たら原因を一緒に切り分ける

\- Windows PowerShell前提でコマンドを書く

\- Codex側で実行確認できる場合は、Codex側でPowerShellから実行する

\- 実行結果を見てから次に進む

\- コードが動いたら、代表ケース・境界値・条件に当てはまらないケースを使って確認する

\- テストケースでは、入力、期待される表示、実際の表示を比べる

\- 私が希望した場合は、Codex側でPowerShellからテストケースを実行して確認する

\- 私が質問して目的がズレそうなときは、次の問いに戻す：



「これは、就活・研究・個人開発で説明できる実装力につながるか？」



\---



\## テストケース確認ルール



\- コードを書いたら、最低2ケースで動作を確認する

\- 条件分岐では、条件に当てはまるケースと当てはまらないケースを確認する

\- 境界値がある場合は、境界の値を必ず確認する

\- 例：60点以上で合格なら、59点、60点、80点などを確認する

\- 繰り返し処理では、0回、1回、複数回の動きを意識して確認する

\- 確認後は、期待どおりだったか、違った場合はどこが違うかを言葉で整理する



\---



\## 進捗更新ルール



各Dayが完了したら、必ず次を行う。



1\. notes/dayX.md を作成・更新する

2\. AGENTS.md の「現在の進捗」を次のDayに更新する

3\. 完了した内容を「完了したこと」に追記する

4\. 次にやることを更新する

5\. 関連ファイルを git add する

6\. commit する



進捗更新をせずに次のDayへ進まない。



\---



\## 現在の進捗



現在は \*\*Day 30：就活用成果物化の完了\*\*。



Day 0、Day 1、Day 2、Day 3、Day 4、Day 5、Day 6、Day 7、Day 8、Day 9、Day 10、Day 11、Day 12、Day 13、Day 14、Day 15、Day 16、Day 17、Day 18、Day 19、Day 20、Day 21、Day 22、Day 23、Day 24、Day 25、Day 26、Day 27、Day 28、Day 29、Day 30は完了済み。



\---



\## 完了したこと



\### Day 0：環境確認



完了したこと：



\- C:\\work\\tech-basic に作業フォルダを作成

\- .venv 作成

\- day0\_check.py 作成・実行

\- .gitignore 作成

\- .venv/ をGit管理から除外

\- Git初回commit済み

\- notes/day0.md 作成済み



学んだこと：



\- PowerShellでPythonファイルを実行する方法

\- git status で状態確認する方法

\- .gitignore の役割

\- .venv/ はGitに入れないこと



\---



\### Day 1：変数・型・print・input



完了したこと：



\- input() で入力を受け取った

\- print() で文字を表示した

\- 変数 name / age / money を使った

\- int(input(...)) で入力を整数に変換した

\- 年齢に 1 を足して来年の年齢を表示した

\- 所持金に 1000 を足した金額を表示した

\- day1.py を作成・実行した

\- notes/day1.md を作成済み

\- Day 1の内容をcommit済み



学んだこと：



\- input() で受け取った値は基本的に文字列になる

\- 数字として計算したい場合は int() で変換する

\- 変数に値を入れると、あとから計算や表示に使える

\- print() では文字列や計算結果を表示できる



\---



\### Day 2：if文



完了したこと：



\- if文を使って条件分岐を書いた

\- 点数を入力して、合格・不合格を判定した

\- elifを使って、点数を3段階で判定した

\- andを使って、年齢と所持金の両方を条件にした

\- day2.py を作成・実行した

\- notes/day2.md を作成済み

\- Day 2の内容をcommit済み



学んだこと：



\- 条件によって実行する処理を変えられる

\- 条件を書く順番も大事

\- if / elif / else で複数の条件を分けられる

\- and は両方の条件を満たすときだけ成り立つ



\---

\### Day 3：for文・while文



完了したこと：



\- for と range() を使って、1から5まで表示した

\- while を使って、1から5まで表示した

\- 0回、1回、複数回の繰り返しを確認した

\- day3.py を作成・実行した

\- notes/day3.md を作成済み

\- Day 3の内容をcommit済み



学んだこと：



\- for は繰り返し処理をしたいときに使う

\- range() は繰り返す範囲を指定するときに使う

\- while は条件が成り立っている間、処理を繰り返す

\- while で値を増やし忘れると、無限ループになる



\---

\### Day 4：list



完了したこと：



\- listを使ってETF名をまとめた

\- append()でETF名を後から追加した

\- len()でETFの数を確認した

\- forでETF名を1つずつ表示した

\- インデックスを使ってリストの要素を確認した

\- 0個、1個、複数個のリストを確認した

\- day4.py を作成・実行した

\- notes/day4.md を作成済み

\- Day 4の内容をcommit済み



学んだこと：



\- listは複数あるものをまとめるもの

\- append()はリストに要素を追加するときに使う

\- len()はリストの中身の数を数えるときに使う

\- インデックスは0から始まる

\- forとlistを組み合わせると、リストの中身を1つずつ処理できる



\---

\### Day 5：dict



完了したこと：



\- dictを使ってETF名と価格をセットで管理した

\- キーを使ってdictから値を取り出した

\- forを使ってdictのキーと値を表示した

\- 代表ケースとしてTOPIXと日経225の表示を確認した

\- day5.py を作成・実行した

\- notes/day5.md を作成済み

\- Day 5の内容をcommit済み



学んだこと：



\- dictはキーと値をセットで扱うもの

\- キーを使うと、対応する値を取り出せる

\- forでdictを回すと、キーを1つずつ取り出せる

\- 値を計算に使う場合は、文字列ではなく数値にする



\---

\### Day 6：関数



完了したこと：



\- defを使って関数を作成した

\- 引数を使ってETF名、価格、口数を受け取った

\- 関数を呼び出してETF名と価格を表示した

\- returnを使って評価額を返した

\- 0口、1口、複数口のケースで評価額を確認した

\- day6.py を作成・実行した

\- notes/day6.md を作成済み

\- Day 6の内容をcommit済み



学んだこと：



\- 関数は、同じような処理を再利用するために使う

\- 引数は、関数の外から受け取る値

\- 関数を呼び出すと、関数の中に書いた処理が実行される

\- returnを使うと、計算結果を関数の外で使える



\---

\### Day 7：例外処理・ログ



完了したこと：



\- try / except を使って、数字に変換できない入力を処理した

\- ETF価格を入力し、数字の場合は価格を表示した

\- 数字ではない入力の場合はエラーメッセージを表示した

\- logging を使って、処理の記録を day7.log に残した

\- 数字の場合と数字ではない場合の2ケースで動作確認した

\- day7.py を作成・実行した

\- notes/day7.md を作成済み

\- Day 7の内容をcommit済み



学んだこと：



\- try の中にエラーが起きそうな処理を書く

\- except ValueError で、数字に変換できない場合の処理を書ける

\- エラー処理を使うと、入力ミスでプログラムが止まるのを防げる

\- logging を使うと、プログラムの処理をファイルに記録できる

\- インデントがずれると IndentationError になる



\---

\### Day 8：テキストファイル読み書き



完了したこと：



\- with open() を使ってテキストファイルを開いた

\- write() を使って etf_memo.txt にETFメモを書き込んだ

\- read() を使って etf_memo.txt の中身を読み込んだ

\- 読み込んだ内容を print() で表示した

\- 1行のケースと2行のケースで動作確認した

\- day8.py を作成・実行した

\- notes/day8.md を作成済み

\- Day 8の内容をcommit済み



学んだこと：



\- open() でファイルを開ける

\- "w" は書き込みモード、"r" は読み込みモード

\- write() はファイルに文字を書き込む

\- read() はファイルの中身を読み込む

\- with を使うと、ファイルを使い終わったあと自動で閉じられる

\- 改行は \n で表せる



\---

\### Day 9：CSV読み書き



完了したこと：



\- csv を使ってCSVファイルを扱った

\- csv.writer を使って etf_prices.csv にETF名と価格を書き込んだ

\- writerow() を使って1行ずつデータを書き込んだ

\- csv.reader を使って etf_prices.csv を読み込んだ

\- row[0] と row[1] を使って、ETF名と価格を表示した

\- 1件、2件、3件のケースで動作確認した

\- day9.py を作成・実行した

\- notes/day9.md を作成済み

\- Day 9の内容をcommit済み



学んだこと：



\- CSVファイルはPythonのプログラムでも扱える

\- csv.writer はCSVに書き込むために使う

\- writerow() はCSVに1行分のデータを書き込む

\- csv.reader はCSVを読み込むために使う

\- 読み込んだ行は row[0]、row[1] のように取り出せる



\---

\### Day 10：JSON読み書き



完了したこと：



\- json を使ってJSONファイルを扱った

\- dictでETF名と価格を管理した

\- json.dump() を使って etf_prices.json にETF名と価格を書き込んだ

\- json.load() を使って etf_prices.json を読み込んだ

\- forで読み込んだデータを1件ずつ表示した

\- TOPIXと日経225の2件で動作確認した

\- day10.py を作成・実行した

\- notes/day10.md を作成済み

\- Day 10の内容をcommit済み



学んだこと：



\- JSONファイルはdictのようなデータを保存するときに使える

\- json.dump() はPythonのデータをJSONファイルに書き込むために使う

\- json.load() はJSONファイルを読み込むために使う

\- 同じキーを2回使うと、後ろの値で上書きされる

\- print(file) ではファイルの中身ではなく、ファイルそのものの情報が表示される



\---

\### Day 11：datetime



完了したこと：



\- datetime.now() を使って現在の日付と時刻を取得した

\- strftime() を使って日付と時刻の表示形式を整えた

\- ETF取引日と記録時刻を表示した

\- day11.py を作成・実行した

\- notes/day11.md を作成済み

\- Day 11の内容をcommit済み



学んだこと：



\- datetime.now() は現在の日付と時刻をまとめて取得する

\- strftime("%Y-%m-%d") で日付を YYYY-MM-DD 形式にできる

\- strftime("%H:%M") で時刻を HH:MM 形式にできる

\- strftime() は単独ではなく、日時データに対して使う



\---

\### Day 12：pandas



完了したこと：



\- pandasを使ってCSVファイルを読み込んだ

\- DataFrameとしてETF価格データを表示した

\- read_csv() を使って etf_prices.csv を読み込んだ

\- df["価格"] を使って価格列だけを取り出した

\- head(2) を使って先頭2行だけを表示した

\- day12.py を作成・実行した

\- etf_prices.csv をDay 12用に見出し付きCSVへ更新した

\- notes/day12.md を作成済み

\- Day 12の内容をcommit済み



学んだこと：



\- pandasを使うとCSVを表形式のデータとして扱える

\- DataFrameは表形式のデータを入れるもの

\- read_csv() はCSVファイルを読み込むために使う

\- head() は先頭の数行だけ確認するときに使う

\- ファイル形式によって読み書きの方法が違うので、何の形式を扱っているかを意識する



\---

\### Day 13：FastAPI入門



完了したこと：



\- FastAPIを使って小さいWebアプリを作成した

\- ブラウザで `/` にアクセスして文字を表示した

\- `uvicorn` を使ってFastAPIアプリを起動した

\- `python day13.py` ではなく `uvicorn day13:app --reload` で起動することを確認した

\- 存在しないURLでは `Not Found` になることを確認した

\- day13.py を作成・実行した

\- notes/day13.md を作成済み

\- Day 13の内容をcommit済み



学んだこと：



\- FastAPIはWebアプリ本体を作るために使う

\- `@app.get("/")` は `/` にGETアクセスされたときの処理を指定する

\- `uvicorn` はFastAPIアプリをサーバーとして起動するために使う

\- `day13:app` は `day13.py` の中の `app` を起動するという意味

\- `--reload` はコードを変更したときに自動で読み直す設定



\---

\### Day 14：GET / POST



完了したこと：



\- FastAPIでGETの処理を書いた

\- FastAPIでPOSTの処理を書いた

\- `/etf` にGETでアクセスしてETF名を返す処理を作った

\- `/etf` にPOSTで送られてきた `name` を受け取る処理を作った

\- GETとPOSTの違いを確認した

\- POSTで `name` がある場合とない場合を確認した

\- day14.py を作成・実行した

\- notes/day14.md を作成済み

\- Day 14の内容をcommit済み



学んだこと：



\- GETは情報を見るときに使う

\- POSTはデータを送るときに使う

\- `@app.post` は送る側ではなく、送られてきたデータを受け取る側

\- 同じURLでもGETとPOSTで処理を分けられる

\- 必要な値が送られていないとFastAPIがエラーにする



\---

\### Day 15：HTML表示



完了したこと：



\- FastAPIでHTMLを返す処理を書いた

\- `HTMLResponse` を使って、HTMLとしてブラウザに表示した

\- `/` にアクセスして、ETF管理アプリの見出しと説明文を表示した

\- `/not-found` にアクセスして、存在しないURLでは `404 Not Found` になることを確認した

\- day15.py を作成・実行した

\- notes/day15.md を作成済み

\- Day 15の内容をcommit済み



学んだこと：



\- HTMLはブラウザに見出しや文章を表示するために使う

\- `HTMLResponse` を使うと、FastAPIからHTMLを返せる

\- `day15:app` は `day15.py` の中の `app` を起動するという意味

\- 存在しないURLにアクセスすると `404 Not Found` になる



\---

\### Day 16：画面整備



完了したこと：



\- FastAPIでHTML画面を少し見やすく整えた

\- `<h1>`、`<p>`、`<h2>`、`<ul>`、`<li>` を使った

\- ETF管理アプリの見出し、説明文、箇条書きを表示した

\- `/` にアクセスしてHTMLが表示されることを確認した

\- `/not-found` にアクセスして、存在しないURLでは `404 Not Found` になることを確認した

\- day16.py を作成・実行した

\- notes/day16.md を作成済み

\- Day 16の内容をcommit済み



学んだこと：



\- HTMLタグを使うと、見出し、文章、箇条書きを分けて表示できる

\- `<h1>` は大きな見出し、`<p>` は文章、`<ul>` と `<li>` は箇条書きに使う

\- FastAPIでHTMLを返すと、ブラウザ上の画面を整えられる

\- サーバーの起動には `uvicorn day16:app --reload` を使う



\---

\### Day 17：SQLite入門



完了したこと：



\- sqlite3 を使ってPythonからSQLiteに接続した

\- etf_app.db というデータベースファイルを作成した

\- connection.close() で接続を閉じた

\- データベースファイルを作ることと、SQLでデータを操作することの違いを確認した

\- day17.py を作成・実行した

\- notes/day17.md を作成済み

\- Day 17の内容をcommit済み



学んだこと：



\- sqlite3 はPythonからSQLiteを使うための道具

\- sqlite3.connect("etf_app.db") でデータベースファイルに接続できる

\- データベースファイルがない場合は、connect() したときに作られる

\- close() でデータベースへの接続を閉じる

\- Day 17では空のデータベースファイルを作り、SQLの操作はDay 18以降で学ぶ



\---

\### Day 18：SELECT / INSERT



完了したこと：



\- CREATE TABLE IF NOT EXISTS を使って etfs テーブルを作成した

\- INSERT を使ってETF名をSQLiteに追加した

\- SELECT を使って保存済みのETF名を取り出した

\- fetchall() を使ってSELECT結果を受け取った

\- commit() を使ってINSERTした内容を保存した

\- 実行するたびにINSERTしたETF名が追加されることを確認した

\- day18.py を作成・実行した

\- notes/day18.md を作成済み

\- Day 18の内容をcommit済み



学んだこと：



\- SQLはデータベースにお願いを出すための文

\- INSERTはデータを追加するときに使う

\- SELECTはデータを取り出すときに使う

\- cursorはSQLを実行するための操作係

\- SQLiteはプログラム終了後もデータをファイルに残す

\- 未説明の関数やSQLは、意味を確認してから書くほうが理解しやすい



\---

\### Day 19：UPDATE / DELETE



完了したこと：



\- UPDATE を使ってETF名を変更した

\- DELETE を使ってETF名を削除した

\- WHERE を使って変更・削除する対象を指定した

\- INSERT、SELECT、UPDATE、DELETE の違いを整理した

\- day19.py を作成・実行した

\- notes/day19.md を作成済み

\- Day 19の内容をcommit済み



学んだこと：



\- INSERT はデータを追加する

\- SELECT はデータを取り出す

\- UPDATE はデータを変更する

\- DELETE はデータを削除する

\- WHERE は変更・削除する対象を指定する

\- WHERE を書かないと全件が対象になるため注意が必要



\---

\### Day 20：FastAPI + SQLite



完了したこと：



\- FastAPIからSQLiteに接続した

\- SELECTでetfsテーブルのETF名を取り出した

\- fetchall() の結果から row[0] を使ってETF名を取り出した

\- 取り出したETF名をlistに追加して、FastAPIのレスポンスとして返した

\- `/etfs` でETF一覧が返ることを確認した

\- `/not-found` で404になることを確認した

\- day20.py を作成・実行した

\- notes/day20.md を作成済み

\- Day 20の内容をcommit済み



学んだこと：



\- FastAPIとSQLiteを組み合わせると、DBのデータをWeb APIとして返せる

\- SELECTで取り出した結果は、forで1件ずつ取り出してlistにすると扱いやすい

\- returnは関数の中に書く必要がある

\- 複数の学習内容を組み合わせるときは、1行ずつ何をしているか確認することが大事



\---

\### Day 21：pytest入門



完了したこと：



\- pytestをインストールした

\- calculate_value 関数を作成した

\- test_day21.py にpytestのテストを書いた

\- assertを使って、期待される結果と実際の結果を確認した

\- 0口、1口、複数口のケースで動作確認した

\- day21.py を作成・実行した

\- test_day21.py を作成・実行した

\- notes/day21.md を作成済み

\- Day 21の内容をcommit済み



学んだこと：



\- pytestはPythonコードの動作を自動で確認するために使う

\- assertは期待する結果と実際の結果を比べるために使う

\- test_ で始まる関数をpytestがテストとして見つける

\- pytestが入っていない場合は pip install pytest でインストールする

\- pytestは python -m pytest で実行できる



\---

\### Day 22：FastAPIのテスト



完了したこと：



\- FastAPIの小さいアプリを作成した

\- TestClientを使って、pytestの中からFastAPIにアクセスした

\- `/` にGETアクセスして、ステータスコード200を確認した

\- `/` のJSONレスポンスが `{"message": "ETF test"}` になることを確認した

\- `/not-found` にGETアクセスして、ステータスコード404を確認した

\- test_day22.py を作成・実行した

\- notes/day22.md を作成済み

\- Day 22の内容をcommit済み



学んだこと：



\- TestClientはFastAPIアプリをテストの中から呼び出すために使う

\- client.get("/") でテストの中からGETアクセスできる

\- status_code の200は成功を表す

\- status_code の404はURLが見つからないことを表す

\- FastAPIのAPIはブラウザだけでなくpytestでも確認できる



\---



\### Day 23：Git基礎



完了したこと：



\- git status を使って変更されたファイルがあるか確認した

\- git add は変更をcommitに入れる準備だと確認した

\- git commit は変更をGitの履歴として記録するためのコマンドだと確認した

\- git status、git add、git commit の流れを整理した

\- notes/day23.md を作成済み

\- Day 23の内容をcommit済み



学んだこと：



\- git status は作業フォルダの状態を確認するために使う

\- git add は変更をcommitに入れる準備をする

\- git commit は変更をGitの履歴として記録する

\- 最後にgit statusでworking tree cleanを確認する



\---

\### Day 24：GitHub公開



完了したこと：



\- GitHubに `tech-basic` リポジトリを作成した

\- `git remote add origin ...` でローカルGitとGitHubリポジトリを接続した

\- `git remote -v` でremoteが登録されたことを確認した

\- `git push -u origin master` でローカルのcommit履歴をGitHubへ送った

\- `git status` で `origin/master` と同期済みであることを確認した

\- notes/day24.md を作成済み

\- Day 24の内容をcommit済み



学んだこと：



\- remote はPCのGitリポジトリとGitHub上のリポジトリをつなぐ接続先

\- push はPCにあるcommit履歴をGitHubへ反映する操作

\- `git add`、`git commit`、`git push` はそれぞれ役割が違う

\- GitHub公開前後は `git status` や `git remote -v` で状態を確認する



\---

\### Day 25：README作成



完了したこと：



\- READMEの役割を確認した

\- 就活用として企業の人が見る前提でREADMEの構成を整理した

\- README.md を作成した

\- 概要、目的、身につけた技術、作成したもの、リポジトリ構成、実行方法、今後の予定を書いた

\- 各Dayのファイルは独立していることをREADMEに書いた

\- notes/day25.md を作成済み

\- Day 25の内容をcommit済み



学んだこと：



\- READMEはGitHubで見た人にリポジトリの内容を伝える説明書になる

\- 就活用READMEでは、何を学んだかだけでなく、何ができるようになったかを書くと伝わりやすい

\- 実行方法を書くときは、リポジトリの構成に合わせて説明する必要がある



\---

\### Day 26：ETFデータ読み込み



完了したこと：



\- pandasを使って `etf_prices.csv` を読み込んだ

\- `ETF名` 列と `価格` 列を取り出して表示した

\- ETFが3件の場合と1件の場合で、必要な列を取り出せることを確認した

\- day26.py と notes/day26.md を作成した

\- Day 26の内容をcommit済み



学んだこと：



\- `pandas.read_csv()` はCSVファイルを表形式のデータとして読み込む

\- `df["列名"]` と書くと、列名で表示する範囲を指定できる



\---



\### Day 27：売買シグナル作成



完了したこと：



\- `get_signal(price)` 関数を作成した

\- 価格が1000未満なら「買い」、1500より大きいなら「売り」、それ以外なら「様子見」を返す条件分岐を書いた

\- 代表ケース、境界値、条件に当てはまらないケースとして900、1000、1500、1600で動作確認した

\- day27.py と notes/day27.md を作成した

\- Day 27の内容をcommit済み



学んだこと：



\- 関数の中でif / elif / elseを使うと、条件に応じた結果をreturnできる

\- 「未満」と「より大きい」の条件では、境界値はelseの処理になる



\---



\### Day 28：損益計算



完了したこと：



\- `calculate_profit(buy_price, current_price, quantity)` 関数を作成した

\- 購入価格・現在価格・口数から損益を計算した

\- 利益、損失、損益ゼロの3ケースで動作確認した

\- day28.py と notes/day28.md を作成した

\- Day 28の内容をcommit済み



学んだこと：



\- 損益は「(現在価格 - 購入価格) × 口数」で計算できる

\- 現在価格が購入価格より高いと利益、低いと損失、同じなら損益ゼロになる



\---

\### Day 29：Web画面統合



完了したこと：



\- FastAPIでHTML画面を表示した

\- ETF名、価格、売買シグナル、損益を1画面に表示した

\- `get_signal(price)` で売買シグナルを作った

\- `calculate_profit(buy_price, price, quantity)` で損益を計算した

\- 代表ケース、境界値、損益の3ケースで動作確認した

\- day29.py と notes/day29.md を作成した

\- Day 29の内容をcommit済み



学んだこと：



\- Pythonで計算した結果をf文字列でHTMLに埋め込める

\- `if` / `elif` / `else` は同じ高さにそろえる

\- 関数に渡す変数名は、実際に定義済みの名前にする必要がある

\- FastAPIでHTMLを返すと、ブラウザで計算結果を確認できる



\---

\### Day 30：就活用成果物化



完了したこと：



\- READMEを就活用に見直した

\- 作成したETF管理アプリで何ができるかを整理した

\- Python、SQLite、FastAPI、HTML、pytest、Git/GitHubで学んだ内容を整理した

\- Codexを学習コーチ、レビュー担当、進捗管理の補助として使ったことを整理した

\- `uvicorn day29:app --reload` の実行方法をREADMEに追加した

\- `day29.py` の売買シグナル、損益計算、Web画面表示を確認した

\- pytestで既存テストが通ることを確認した

\- notes/day30.md を作成した

\- Day 30の内容をcommit済み



学んだこと：



\- READMEでは、最初に「何を作ったか」「何ができるか」「使った技術」を伝えると分かりやすい

\- 就活用の説明では、学習した順番だけでなく、成果物として説明できる形に整理することが大事

\- Codexを使う場合でも、自分で実装し、実行結果を確認し、学習記録を残すことで説明できる経験になる

\- READMEの見出しは、現在の進捗と時制が合うように書く必要がある



\---

\## 次にやること



Day 0からDay 30までの学習ロードマップは完了。



次は必要に応じて、GitHubへpushし、READMEを見た人に伝わるかを確認する。



追加で改善する場合は、日本ETFペーパートレード管理アプリとして次の機能を広げる。



\- ETFデータをCSVやSQLiteからWeb画面に表示する

\- 売買記録を追加、編集、削除できるようにする

\- 損益の履歴を一覧で確認できるようにする



\---



\## Day 27の進め方



\### 最初にやる復習



Day 26の復習として、次を確認する。



\- `pandas.read_csv()` は何をするか

\- `df["ETF名"]` は何を取り出すか

\- `df["価格"]` は何を取り出すか

\- 1件だけのCSVでも列を取り出せるか



\### 使い方の小さい例



価格を受け取り、条件に応じて文字を返すif文の小さい例を1つだけ見せる。



例：



ETF価格が基準より低い場合に、買いシグナルを返す。



\### その後の問題



似た問題として、ETF管理アプリ用のデータを1件変更または削除する処理を私に書かせる。



\---



\## 学習記録テンプレート



各Dayの最後に、notes/dayX.md を作る。



形式：



\# Day X 学習記録



\## 今日やったこと



\-


\## 詰まったところ



\-



\---



\## Git運用ルール



各Dayの最後に、必ず次を行う。



git status  

git add 関連ファイル  

git commit -m "Complete day X"  

git status  



例：



git add day2.py notes/day2.md AGENTS.md  

git commit -m "Complete day 2"  

git status  



最後に working tree clean になっていることを確認する。



\---



\## 注意



このAGENTS.mdは、学習の進捗に合わせて更新する。  

特に「現在の進捗」「完了したこと」「次にやること」は、各Day完了時に必ず更新する。

