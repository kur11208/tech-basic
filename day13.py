# Day 13: FastAPI入門

# ここにFastAPIの小さいWebアプリを書いていきます。
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "ETF管理アプリへようこそ"