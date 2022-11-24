#!/usr/bin/python3
# Test case for multiply two numbers
import unittest
from multiply import Mul

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 0,3,12]
        result = Mul(data)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
