import sqlite3


# Day 18: SELECT / INSERT
# ここに、SQLiteへデータを追加して取り出す練習コードを書きます。
connection = sqlite3.connect("etf_app.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS etfs (name TEXT)")
cursor.execute("INSERT INTO etfs (name) VALUES (?)", ("TOPIX",))
cursor.execute("SELECT name FROM etfs")
rows = cursor.fetchall()
for row in rows:
    print(row[0])
connection.commit()
connection.close()
