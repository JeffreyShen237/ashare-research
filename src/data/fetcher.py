import akshare as ak
from storage import save_price

def get_prefix(stock_code):
    if stock_code.startswith("6"):
        return "sh" + stock_code
    else:
        return "sz" + stock_code

def fetch_constituents():
    df = ak.index_stock_cons(symbol="000906")
    return df

def fetch_price(stock_code):
    symbol = get_prefix(stock_code)
    df = ak.stock_zh_a_daily(
        symbol=symbol, 
        adjust="qfq",
    )
    return df

def fetch_all_prices(stock_codes):
    for code in stock_codes:
        try:
            df = fetch_price(code)
            if df is not None and not df.empty:
                save_price(code, df)
            else:
                print(f"{code} 数据为空，跳过")
        except Exception as e:
            print(f"{code} 失败: {e}")

constituents = fetch_constituents()
codes = constituents["品种代码"].tolist()
fetch_all_prices(codes)