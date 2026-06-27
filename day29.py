from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

etf_name = "TOPIX ETF"
price = 1200
buy_price = 1000
quantity = 10


@app.get("/", response_class=HTMLResponse)
def index():
    signal = get_signal(price)
    profit = calculate_profit(buy_price, price, quantity)
    html = f"""
    <html>
        <body>
            <h1>ETF管理アプリ</h1>
            <p>ETF名:{etf_name}</p>
            <p>価格:{price}</p>
            <p>売買シグナル:{signal}</p>
            <p>損益:{profit}</p>
        </body>
    </html>
    """
    return html


def get_signal(price):
    if price < 1000:
        return "買い"
    elif price > 1500:
        return "売り"
    else:
        return "様子見"


def calculate_profit(buy_price, price, quantity):
    return (price-buy_price)*quantity
