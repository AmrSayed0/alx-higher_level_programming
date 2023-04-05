#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test for a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    
    def test_empty_list(self):
        """Test for an empty list"""
        self.assertIsNone(max_integer([]))
    
    def test_one_element_list(self):
        """Test for a list with a single element"""
        self.assertEqual(max_integer([42]), 42)
    
    def test_identical_elements(self):
        """Test for a list with identical elements"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
    
    def test_negative_elements(self):
        """Test for a list with negative elements"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)
    
    def test_mixed_elements(self):
        """Test for a list with mixed positive and negative elements"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
    
    def test_not_a_list(self):
        """Test for a parameter that is not a list"""
        with self.assertRaises(TypeError):
            max_integer("hello")
