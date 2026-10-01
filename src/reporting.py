from src import portfolio
from typing import List
import pandas as pd

def generate_report(results: List[List[float]]) -> pd.DataFrame:
    report_data = []
    for result in results:
        asset_values = {asset.name: value for asset in portfolio.from_csv('data/sample_investments.csv').assets}
        report_data.append({asset: asset_values[asset] for asset in asset_values})
    return pd.DataFrame(report_data)

    def save_report(self, filepath: str) -> None:
        # Save the report to a CSV file
        pass

    def load_report(self, filepath: str) -> pd.DataFrame:
        return pd.read_csv(filepath)

    def __str__(self):
        return self.generate_report().to_string()