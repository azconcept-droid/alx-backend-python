#!/usr/bin/env python3
""" Parameterize and patch as decorators
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
)


class TestAccessNestedMap(unittest.TestCase):
    """ Class to test access nested map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any):
        """ method to test access nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected)
