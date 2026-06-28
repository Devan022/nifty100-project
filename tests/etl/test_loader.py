from src.etl.loader import ExcelLoader

loader = ExcelLoader()

datasets = loader.load_all()

print("=" * 50)

print("Datasets Loaded")

print("=" * 50)

for name, sheets in datasets.items():
    print(f"{name} : {len(sheets)} sheet(s)")