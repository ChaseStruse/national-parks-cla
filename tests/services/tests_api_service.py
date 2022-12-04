import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from src.services.api_service import ApiService
from src.services.data_conversion_service import DataConversionService


class TestApiService(TestCase):
    def setUp(self):
        self._sut = ApiService('test_key')

    def test_get_parks_by_state_returns_dict_from_data_conversion_service(self):
        expected = {'Test Park': 'Test description', 'Test Park 2': 'Test Description 2'}
        DataConversionService.convert_parks_json_to_name_description_dict = MagicMock(return_value=expected)
        actual = self._sut.get_parks_by_state('IA')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()