#!/usr/bin/env python3
""" Unit tests for functions in `utils` module
"""

from parameterized import parameterized
import unittest

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Unit test class for `access_nested_map` function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Testing that `access_nested_map` function returns expected value
        when given a nested map with a path of map keys
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Testing that `access_nested_map` function raises the right exception
        when given invalid paths, and the right exception message
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")
