import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from aesjosephus import avalanche, time
import unittest

class TestNoErrorEEE(unittest.TestCase):
    def test_avalanche_and_time(self):
        row = 10
        avalanche.avalanche_df(row)
        time.time_df(row)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()