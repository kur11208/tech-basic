import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get("/etfs")
def show_etfs():
    connection = sqlite3.connect("etf_app.db")
    cursor = connection.cursor()
    # Fresh clones have no runtime database; build the empty teaching schema safely.
    cursor.execute("CREATE TABLE IF NOT EXISTS etfs (name TEXT)")
    cursor.execute("SELECT name FROM etfs")
    rows = cursor.fetchall()
    names = []
    for row in rows:
        names.append(row[0])
    connection.close()
    return {"etfs": names}