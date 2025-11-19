import pandas as pd
from typing import Dict

def load_sheets(file_path: str) -> Dict[str, pd.DataFrame]:
    """Load all sheets from an Excel file as a dictionary of DataFrames."""
    try:
        return pd.read_excel(file_path, sheet_name=None)
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return {}

EDINBURGH_PATH = "data/Edinburgh-daytime.xlsx"
EDINBURGH_SHEET = load_sheets(EDINBURGH_PATH )

#If we selected one specific sheet within the Excel file
#return pd.read_excel(file_path, sheet_name='1112')
print(EDINBURGH_SHEET.head())
