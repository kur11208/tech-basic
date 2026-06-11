import sqlite3


# Day 19: UPDATE / DELETE
# ここに、SQLiteのデータを変更・削除する練習コードを書きます。

connection = sqlite3.connect("etf_app.db")
cursor = connection.cursor()
cursor.execute("UPDATE etfs SET name = ? WHERE name = ?", ("日経225", "TOPIX"))
cursor.execute("INSERT INTO etfs (name) VALUES (?)", ("削除練習ETF",))
cursor.execute("DELETE FROM etfs WHERE name = ?", ("削除練習ETF",))
connection.commit()
cursor.execute("SELECT name FROM etfs")
rows = cursor.fetchall()
for row in rows:
    print(row[0])
connection.close()