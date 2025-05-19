#!/usr/bin/env python3
""" Unit tests for functions in `utils` module
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """ Unit test class for `access_nested_map` function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any
            ) -> None:
        """Testing that `access_nested_map` function returns expected value"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Testing that `access_nested_map` function raises the right exception
        when given invalid paths, and the right exception message
        """
        with self.assertRaises(expected) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Unit test class for `get_json` function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        """
        Testing that `get_json` function returns the expected payload
        from URL
        """
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload

            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Unit test class for `memoize` decorator
    """
    def test_memoize(self):
        """ Testing that `memoize` decorator works for memoization
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with (patch.object(TestClass, 'a_method', return_value=42)
              as mock_method):
            test_object = TestClass()

            result1 = test_object.a_property
            result2 = test_object.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
