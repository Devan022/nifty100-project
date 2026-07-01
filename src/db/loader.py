from pathlib import Path
import sqlite3
import pandas as pd

from src.etl.loader import ExcelLoader
from src.etl.normaliser import DataNormaliser

class DatabaseLoader:
    """
    Loads all cleaned Excel data into the SQLite database.
    """

    def __init__(self, db_path="db/nifty100.db"):
        self.db_path = Path(db_path)
        self.connection = sqlite3.connect(self.db_path)
        self.loader = ExcelLoader()
        self.normaliser = DataNormaliser()
    def load_all(self):
        datasets = self.loader.load_all()

        for table_name, sheets in datasets.items():

            # Each workbook currently has one sheet
            for sheet_name, dataframe in sheets.items():

                print("\n==============================")
                print(f"TABLE : {table_name}")
                print(f"SHEET : {sheet_name}")
                print("==============================")

                print("\nColumns:")
                print(dataframe.columns.tolist())

                print("\nFirst 5 rows:")
                print(dataframe.head())
                dataframe = self.normaliser.clean_dataframe(dataframe)
                print(f"Rows before to_sql: {len(dataframe)}")
                print(dataframe.head())
                dataframe.to_sql(
                    name=table_name,
                    con=self.connection,
                    if_exists="replace",
                    index=False
                )
                count = pd.read_sql_query(
                    f"SELECT COUNT(*) AS cnt FROM {table_name}",
                    self.connection
                )

                print(count)

                print(f"\nLoaded {len(dataframe)} rows into '{table_name}'")

        self.connection.commit()
        self.connection.close()

        print("\nAll tables loaded successfully!")
        if __name__ == "__main__":
            loader = DatabaseLoader()
            loader.load_all()