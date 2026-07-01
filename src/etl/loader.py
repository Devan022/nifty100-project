from pathlib import Path
import pandas as pd


class ExcelLoader:
    """
    Loads all Excel datasets from data/raw.
    """

    def __init__(self, data_dir="data/raw"):
        self.data_dir = Path(data_dir)

    def load_file(self, filename):
        file_path = self.data_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found.")

        # Files whose headers start on Excel row 2
        header1_files = {
            "cashflow.xlsx",
            "balancesheet.xlsx",
            "profitandloss.xlsx",
            "analysis.xlsx",
            "documents.xlsx",
            "prosandcons.xlsx",
            "companies.xlsx",
        }

        # Files whose headers start on Excel row 1
        header0_files = {
            "financial_ratios.xlsx",
            "stock_prices.xlsx",
            "sectors.xlsx",
            "peer_groups.xlsx",
            "market_cap.xlsx",
        }

        if filename in header1_files:
            header = 1
        elif filename in header0_files:
            header = 0
        else:
            header = 0
        print(f"{filename=} {header=}")
        return pd.read_excel(
            file_path,
            sheet_name=None,
            header=header
        )
    def load_all(self):
        """
        Load every Excel file inside data/raw.
        """

        datasets = {}

        for file in self.data_dir.glob("*.xlsx"):
            datasets[file.stem] = self.load_file(file.name)

        return datasets