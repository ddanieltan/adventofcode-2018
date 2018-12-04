import unittest
from solve import calc

class TestCases(unittest.TestCase):
    """Tests for Day 01"""

    def test1(self):
        test_input=['+1', '+1', '+1']
        self.assertEqual(calc(test_input),3)

    def test2(self):
        test_input=['+1', '+1', '-2']
        self.assertEqual(calc(test_input),0)
    
    def test3(self):
        test_input=['-1', '-2', '-3']
        self.assertEqual(calc(test_input),-6)

if __name__=="__main__":
    unittest.main()