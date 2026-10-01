import unittest
from src import tax_loss_harvesting
from src.utils import read_csv

class TestTaxLossHarvesting(unittest.TestCase):
    def setUp(self):
        self.portfolio = tax_loss_harvesting.PortfolioTaxLossHarvesting(read_csv('data/sample_investments.csv'))

    def test_harvest_strategy(self):
        self.portfolio.harvest_strategy()
        self.assertEqual(len(self.portfolio.tax_loss_harvested), 0)
        # More complex tests would be needed here

    def test_update_portfolio(self):
        self.portfolio.update_portfolio()
        self.assertEqual(len(self.portfolio.assets), 0)
        # More complex tests would be needed here

if __name__ == '__main__':
    unittest.main()