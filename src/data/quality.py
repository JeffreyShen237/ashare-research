from pathlib import Path

def check_quality(price_dir):
    files = list(Path(price_dir).glob("*.parquet"))
    print(f"成功存储：{len(files)} 只股票")
    
    import pandas as pd
    short_data = []
    
    for f in files:
        df = pd.read_parquet(f)
        if len(df) < 100:
            short_data.append((f.stem, len(df)))
    
    print(f"数据少于100条的股票：{len(short_data)} 只")
    for code, count in short_data:
        print(f"  {code}: {count} 条")

check_quality("data/raw/prices")