import pandas as pd
from pathlib import Path

def save_price(stock_code, df):
    path = Path(f"data/raw/prices/")
    path.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path / f"{stock_code}.parquet")
    print(f"Data of {stock_code} has been saved to {path / f"{stock_code}.parquet"}")