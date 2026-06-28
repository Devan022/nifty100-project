from pathlib import Path
import sqlite3
import pandas as pd

from src.etl.loader import ExcelLoader


class DatabaseLoader:

    def __init__(self,
                 db_path="db/nifty100.db"):

        self.db_path = Path(db_path)

        self.connection = sqlite3.connect(self.db_path)

        self.loader = ExcelLoader()

    def load_all(self):

        datasets = self.loader.load_all()

        for table_name, sheets in datasets.items():

            for sheet_name, dataframe in sheets.items():

                print("\n====================")
                print(table_name)
                print(dataframe.columns.tolist())
                print("====================")

                dataframe.to_sql(
                    table_name,
                    self.connection,
                    if_exists="append",
                    index=False
                )

                print(f"Loaded {table_name}")

        self.connection.commit()

        self.connection.close()