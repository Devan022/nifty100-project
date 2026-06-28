import pandas as pd


class DataValidator:

    def __init__(self):
        self.failures = []

    def add_failure(self, rule, table, row, column, message):
        self.failures.append({
            "rule": rule,
            "table": table,
            "row": row,
            "column": column,
            "message": message
        })
    def check_duplicate_company_id(self, dataframe):

        duplicates = dataframe[dataframe.duplicated(subset=["id"], keep=False)]

        for index, row in duplicates.iterrows():

            self.add_failure(
                "DQ-01",
                "companies",
                index,
                "company_id",
                "Duplicate Company ID"
            )

    def export_failures(self, output_path):
        df = pd.DataFrame(self.failures)
        df.to_csv(output_path, index=False)

        print(f"Validation report saved to {output_path}")
