from fastapi import FastAPI

app = FastAPI()


# 問題:
# /etf にGETでアクセスされたら {"name": "TOPIX ETF"} を返す処理を書く
@app.get("/etf")
def name():
    return {"name": "TOPIX ETF"}

@app.post("/etf")
def post(name: str):
    return {"message": name + "を受け取りました"}