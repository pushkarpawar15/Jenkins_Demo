#!/usr/bin/python3
# Test case for multiply two numbers
import unittest
from multiply import Mul

class TestSum(unittest.TestCase):
    def test_list_int3(self):
        """
        Test case to add two numbers
        """
        data = [20, 30]
        result = Mul(data)
        self.assertEqual(result, 6)

    def test_list_int4(self):
        """
        Test case to add two numbers
        """
        data = [20, 30]
        result = Mul(data)
        self.assertEqual(result, 6)

    
    

if __name__ == '__main__':
    unittest.main()
