from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    html = "<h1>日本ETFペーパートレード管理アプリ</h1>""<p>ETFの売買練習を記録するアプリです。</p>""<h2>できること</h2>""<ul><li>ETF名を表示する</li><li>購入口数を確認する</li><li>損益を確認する</li></ul>"
    return html
