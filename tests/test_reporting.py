import unittest
from src import reporting
from src.utils import read_csv

class TestReporting(unittest.TestCase):
    def setUp(self):
        self.results = read_csv('data/sample_reports.csv')

    def test_generate_report(self):
        report = reporting.generate_report(self.results)
        self.assertIsNotNone(report)
        # More complex tests would be needed here

if __name__ == '__main__':
    unittest.main()