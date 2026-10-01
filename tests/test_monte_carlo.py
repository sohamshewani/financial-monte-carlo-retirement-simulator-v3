import unittest
from src import monte_carlo
from src.utils import read_csv

class TestMonteCarlo(unittest.TestCase):
    def setUp(self):
        self.portfolio = monte_carlo.PortfolioMonteCarlo(read_csv('data/sample_investments.csv'))

    def test_simulation(self):
        results = self.portfolio.run_simulation(1000)
        self.assertEqual(len(results), 1000)

    def test_save_results(self):
        results = self.portfolio.run_simulation(1000)
        self.portfolio.save_results('test_results.csv')
        self.assertTrue(self.portfolio.check_file_exists('test_results.csv'))

    def test_load_results(self):
        results = self.portfolio.run_simulation(1000)
        self.portfolio.save_results('test_results.csv')
        loaded_results = self.portfolio.load_results('test_results.csv')
        self.assertEqual(len(results), len(loaded_results))

if __name__ == '__main__':
    unittest.main()