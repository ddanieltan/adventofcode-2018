import unittest
from solve import calc, calc_repeat


class TestCases(unittest.TestCase):
    """Tests for Day 01"""

    # Part 1
    def test1(self):
        test_input = ["+1", "+1", "+1"]
        self.assertEqual(calc(test_input), 3)

    def test2(self):
        test_input = ["+1", "+1", "-2"]
        self.assertEqual(calc(test_input), 0)

    def test3(self):
        test_input = ["-1", "-2", "-3"]
        self.assertEqual(calc(test_input), -6)

    # Part 2
    def test4(self):
        test_input = ["+1", "-1"]
        self.assertEqual(calc_repeat(test_input), 0)

    def test5(self):
        test_input = ["+3", "+3", "+4", "-2", "-4"]
        self.assertEqual(calc_repeat(test_input), 10)

    def test6(self):
        test_input = ["-6", "+3", "+8", "+5", "-6"]
        self.assertEqual(calc_repeat(test_input), 5)

    def test7(self):
        test_input = ["+7", "+7", "-2", "-7", "-4"]
        self.assertEqual(calc_repeat(test_input), 14)


if __name__ == "__main__":
    unittest.main()

