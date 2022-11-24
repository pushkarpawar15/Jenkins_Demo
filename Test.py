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

    def test_list_int1(self):
        """
        Test case to add two numbers
        """
        data = [1,2,3,4]
        result = Mul(data)
        self.assertEqual(result, 24)
    
    def test_list_int2(self):
        """
        Test case to add two numbers
        """
        data = [20, 0,3,12]
        result = Mul(data)
        self.assertEqual(result, 0)

    def test_list_int3(self):
        """
        Test case to add two numbers
        """
        data = [20, 30]
        result = Mul(data)
        self.assertEqual(result, 0)

    def test_list_int4(self):
        """
        Test case to add two numbers
        """
        data = [20, 30]
        result = Mul(data)
        self.assertEqual(result, 6)

    
    

if __name__ == '__main__':
    unittest.main()
