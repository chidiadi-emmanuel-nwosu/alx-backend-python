#!/usr/bin/env python3
""" unittest for utils
"""
from typing import Mapping, Any, Sequence, Dict, Callable
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """ test cases for access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any) -> None:
        """ assertEqual for access_nested_map fn
        """
        _result = access_nested_map(nested_map, path)
        self.assertEqual(_result, result)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """ assertRaises for access_nested_map fn
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ test cases for get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """ assertEqual for get_json
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get',
                   return_value=mock_response) as mock_requests_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ test cases for memoize
    """

    def test_memoize(self) -> None:
        """ test memoize
        """
        class TestClass:
            """ test class
            """

            def a_method(self):
                """ a_method
                """
                return 42

            @memoize
            def a_property(self):
                """ a_property
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_instance = TestClass()
            mock_response = Mock()
            mock_response.return_value = 42
            mock_a_method.return_value = mock_response

            result_1 = test_instance.a_property()
            result_2 = test_instance.a_property()

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
