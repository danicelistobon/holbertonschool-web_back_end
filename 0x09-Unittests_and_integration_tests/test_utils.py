#!/usr/bin/env python3
""" Unittests and Integration Tests
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """ Class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, exp):
        """ Test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), exp)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Use the assertRaises context manager to test that a KeyError
            is raised
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test that utils.get_json returns the expected result
        """
        mock_get.return_value = test_payload
        actual_result = get_json(test_url)
        self.assertEqual(actual_result, test_payload)
