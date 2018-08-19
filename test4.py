from unittest import TestCase
from unittest.mock import patch

def mock_diff(a, b):
    # mock diff function completeley opposite i.e. subtracts now
    return a - b

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', side_effect=mock_diff)
    def test_sum(self, summm):
        self.assertEqual(summm(7,3), 4)
        self.assertEqual(summm(9,3), 6)

