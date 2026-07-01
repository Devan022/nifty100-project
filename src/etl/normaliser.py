import re
import pandas as pd


class DataNormaliser:
    """
    Handles data cleaning and normalization.
    """

    @staticmethod
    def normalize_year(year):
        """
        Convert different year formats into integer years.
        Examples:
        2023 -> 2023
        FY2023 -> 2023
        Mar 2024 -> 2024
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

    def clean_dataframe(self, df):
        """
        Generic dataframe cleaning.
        """

        # Remove completely empty rows
        df = df.dropna(how="all")

        # Strip whitespace from text columns
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].astype(str).str.strip()

        # Normalize company IDs
        if "company_id" in df.columns:
            df["company_id"] = df["company_id"].apply(self.normalize_ticker)

        # Normalize years
        if "year" in df.columns:
            df["year"] = df["year"].apply(self.normalize_year)

        # Remove duplicate company-year records
        if "company_id" in df.columns and "year" in df.columns:
            before = len(df)

            df = df.drop_duplicates(
                subset=["company_id", "year"],
                keep="first"
            )

            removed = before - len(df)

            print(f"Removed {removed} duplicate rows.")

        return df.reset_index(drop=True)