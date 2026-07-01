import sqlite3
import pandas as pd
import os

class Analytics:

    def __init__(self, db_path="db/nifty100.db"):

        print("DATABASE =", os.path.abspath(db_path))

        self.connection = sqlite3.connect(db_path)
        print(self.connection.execute("SELECT COUNT(*) FROM market_cap").fetchone())
        print(self.connection.execute("SELECT COUNT(*) FROM financial_ratios").fetchone())

    def query(self, sql):
        return pd.read_sql_query(sql, self.connection)

    def top_market_cap(self):

        sql = """
        SELECT
            company_id,
            year,
            market_cap_crore
        FROM market_cap
        ORDER BY market_cap_crore DESC
        LIMIT 10;
        """

        return self.query(sql)

    def average_roe(self):

        sql = """
        SELECT
            AVG(return_on_equity_pct) AS average_roe
        FROM financial_ratios;
        """

        return self.query(sql)

    def close(self):
        self.connection.close()