from src.etl.loader import ExcelLoader
from src.etl.validator import DataValidator

# Load all datasets
loader = ExcelLoader()
datasets = loader.load_all()

# Get the companies dataset
df = datasets["companies"]

# Create validator
validator = DataValidator()

# Run duplicate company ID check
validator.check_duplicate_company_id(df)

# Export report
validator.export_failures("output/validation_failures.csv")

# Print failures
print("\nValidation Failures:")
for failure in validator.failures:
    print(failure)