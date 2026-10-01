import numpy as np
from src import portfolio
from src.utils import read_csv
from src.utils import write_csv
from typing import List

class PortfolioMonteCarlo:
    def __init__(self, portfolio: portfolio.Portfolio):
        self.portfolio = portfolio
        self.results = []

    def run_simulation(self, num_simulations: int) -> List[List[float]]:
        for _ in range(num_simulations):
            self.portfolio = self.portfolio.from_csv('data/sample_investments.csv')
            annual_returns = np.random.normal(0.05, 0.1, 10)
            for i, asset in enumerate(self.portfolio.assets):
                asset.value *= (1 + annual_returns[i])
            self.results.append([asset.value for asset in self.portfolio.assets])
        return self.results

    def save_results(self, filepath: str) -> None:
        write_csv(pd.DataFrame(self.results), filepath)

    def load_results(self, filepath: str) -> List[List[float]]:
        return list(read_csv(filepath).values.tolist())

    @staticmethod
def check_file_exists(filepath: str) -> bool:
        import os
        return os.path.exists(filepath)