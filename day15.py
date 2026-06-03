from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>日本ETFペーパートレード管理アプリ</h1><p>ETFの売買を記録するアプリです。</p>"
