import pandas as pd

for h in [0, 1, 2, 3]:
    print("\n==========================")
    print("HEADER =", h)
    print("==========================")

    df = pd.read_excel(
        "data/raw/stock_prices.xlsx",
        sheet_name="Sheet1",
        header=h
    )

    print(df.columns.tolist())
    print(df.head())