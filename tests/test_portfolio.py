import unittest
from src import portfolio
from src.utils import read_csv

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.portfolio = portfolio.Portfolio()

    def test_initialization(self):
        self.assertIsNotNone(self.portfolio)

    def test_add_asset(self):
        self.portfolio.add_asset('asset1', 1000)
        self.assertIn('asset1', self.portfolio.assets)

    def test_remove_asset(self):
        self.portfolio.add_asset('asset1', 1000)
        self.portfolio.remove_asset('asset1')
        self.assertNotIn('asset1', self.portfolio.assets)

    def test_total_value(self):
        self.portfolio.add_asset('asset1', 1000)
        self.assertEqual(self.portfolio.total_value(), 1000)

if __name__ == '__main__':
    unittest.main()