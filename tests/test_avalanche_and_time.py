import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from aesjosephus import avalanche, time
import unittest

class TestNoException(unittest.TestCase):
    def test_avalanche_and_time(self):
        row = 10
        avalanche.avalanche_df(row)
        time.time_df(row)

class TestAvalancheEffect(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(avalanche.avalanche("abcd","abcd"), 0)
        self.assertEqual(avalanche.avalanche("abcd","abce"), 1/32)
        self.assertEqual(avalanche.avalanche("abcd","efgh"), 5/32)
    

if __name__ == "__main__":
    unittest.main()