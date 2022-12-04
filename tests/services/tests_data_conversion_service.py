import json
import unittest
from unittest import TestCase
from src.services.data_conversion_service import DataConversionService


class TestDataConversionService(TestCase):
    def setUp(self):
        self._sut = DataConversionService()

    def test_given_valid_json_convert_parks_json_to_name_description_dict_returns_valid_data(self):
        test_json = ('{ "data": [{ "fullName": "Test Park", "description": "Test Description" }, '
                     '{ "fullName": "Test Park 2", "description": "Test Description 2" }] }')

        expected = {'Test Park': 'Test Description', 'Test Park 2': 'Test Description 2'}
        actual = self._sut.convert_parks_json_to_name_description_dict(json.loads(test_json))
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
