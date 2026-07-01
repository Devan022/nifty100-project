import pandas as pd

df = pd.read_excel(
    "data/raw/cashflow.xlsx",
    sheet_name="Cash Flow",
    header=1
)

print("Total rows:", len(df))

duplicates = df[df.duplicated(subset=["company_id", "year"], keep=False)]

print("\nDuplicate rows:")
print(duplicates)

print("\nNumber of duplicates:", len(duplicates))
import pandas as pd

df = pd.read_excel(
    "data/raw/cashflow.xlsx",
    sheet_name="Cash Flow",
    header=1
)

print(df.duplicated(subset=["company_id", "year"]).sum())