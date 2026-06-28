import re
import pandas as pd


class DataNormaliser:

    @staticmethod
    def normalize_year(year):
        """
        Convert different year formats into integer years.
        Examples:
        2023 -> 2023
        FY2023 -> 2023
        FY 2023 -> 2023
        """

        if pd.isna(year):
            return None

        year = str(year).strip().upper()

        match = re.search(r'(\d{4})', year)

        if match:
            return int(match.group(1))

        return None


    @staticmethod
    def normalize_ticker(ticker):
        """
        Normalize stock ticker symbols.
        """

        if pd.isna(ticker):
            return None

        ticker = str(ticker).strip().upper()

        ticker = ticker.replace(".NS", "")
        ticker = ticker.replace(".BO", "")

        ticker = ticker.replace(" ", "")

        return ticker