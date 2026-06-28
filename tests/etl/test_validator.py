from pathlib import Path
import pandas as pd

file_path = Path("data/raw/companies.xlsx")

for h in [0, 1, 2, 3, 4, 5]:
    print("\n" + "=" * 60)
    print(f"HEADER = {h}")
    print("=" * 60)

    try:
        df = pd.read_excel(
            file_path,
            sheet_name="Companies",
            header=h
        )

        print(df.head(5))
        print("\nColumns:")
        print(df.columns.tolist())

    except Exception as e:
        print(e)