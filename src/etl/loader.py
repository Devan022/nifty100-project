from pathlib import Path
import pandas as pd


class ExcelLoader:
    """
    Loads all Excel datasets from data/raw.
    """

    def __init__(self, data_dir="data/raw"):
        self.data_dir = Path(data_dir)

    def load_file(self, filename):
        """
        Load one Excel file.
        """

        file_path = self.data_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found.")

        return pd.read_excel(
    file_path,
    sheet_name=None,
    header=0
)

    def load_all(self):
        """
        Load every Excel file inside data/raw.
        """
        datasets = {}

        for file in self.data_dir.glob("*.xlsx"):
            datasets[file.stem] = self.load_file(file.name)

        return datasets