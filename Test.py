#!/usr/bin/python3
# Test case for multiply two numbers
import unittest
from multiply import Mul

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 30]
        result = Mul(data)
        self.assertEqual(result, 600)

if __name__ == '__main__':
    unittest.main()
