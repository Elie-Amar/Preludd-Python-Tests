import unittest

from leap import is_leap_year


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0

class LeapTest(unittest.TestCase):
    def test_year_not_divisible_by_4(self):
        self.assertIs(is_leap_year(2015), False)

    def test_year_divisible_by_4_not_divisible_by_100(self):
        self.assertIs(is_leap_year(1996), True)

    def test_year_divisible_by_100_not_divisible_by_400(self):
        self.assertIs(is_leap_year(2100), False)

    def test_year_divisible_by_400(self):
        self.assertIs(is_leap_year(2000), True)

    def test_year_negative_4(self):
        self.assertIs(is_leap_year(-4), True)

    def test_year_0(self):
    	self.assertIs(is_leap_year(0), False)
if __name__ == '__main__':
    unittest.main()
