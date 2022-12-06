import json
import unittest
from unittest import TestCase

from src.classes.national_park import NationalPark
from src.classes.national_park_amenity import NationalParkAmenity
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

    def test_given_one_park_convert_parks_json_to_national_park_object_returns_correct_object(self):
        test_json = ('{ "total": "1", "data": [{ "fullName": "Test Park", "description": "Test Description", '
                     '"activities": [{ "name": "act1" }, { "name": "act2" }, { "name": "act3" }] }] }')
        activity_list = ["act1", "act2", "act3"]
        expected = NationalPark("Test Park", "Test Description", activity_list)
        actual = self._sut.convert_parks_json_to_national_park_object(json.loads(test_json), "Test Name")
        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.description, actual.description)
        self.assertEqual(expected.activities, actual.activities)

    def test_given_two_parks_convert_parks_json_to_national_park_object_returns_correct_object(self):
        test_json = ('{ "total": "2", "data": [{ "fullName": "Test Park", "description": "Test Description", '
                     '"activities": [{ "name": "act1" }, { "name": "act2" }, { "name": "act3" }] },'
                     '{"fullName": "Test Park 2", "description": "Test Description 2", '
                     '"activities": [{ "name": "act10" }, { "name": "act20" }, { "name": "act30" }]} ] }')
        activity_list = ["act10", "act20", "act30"]
        expected = NationalPark("Test Park 2", "Test Description 2", activity_list)
        actual = self._sut.convert_parks_json_to_national_park_object(json.loads(test_json), "Test Park 2")
        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.description, actual.description)
        self.assertEqual(expected.activities, actual.activities)

    def test_given_incorrect_name_convert_parks_json_to_national_park_object_returns_empty_object(self):
        test_json = ('{ "total": "2", "data": [{ "fullName": "Test Park", "description": "Test Description", '
                     '"activities": [{ "name": "act1" }, { "name": "act2" }, { "name": "act3" }] },'
                     '{"fullName": "Test Park 2", "description": "Test Description 2", '
                     '"activities": [{ "name": "act10" }, { "name": "act20" }, { "name": "act30" }]} ] }')
        expected = NationalPark()
        actual = self._sut.convert_parks_json_to_national_park_object(json.loads(test_json), "Null Park")
        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.description, actual.description)
        self.assertEqual(expected.activities, actual.activities)

    def test_given_one_park_get_park_code_from_parks_json_returns_correct_park_code(self):
        test_json = '{ "total": "1", "data": [{ "fullName": "Test Park", "parkCode":"cOdE" }] }'
        expected = 'cOdE'
        actual = self._sut.get_park_code_from_parks_json(json.loads(test_json), 'Test Park')
        self.assertEqual(expected, actual)

    def test_given_two_parks_get_park_code_from_parks_json_returns_correct_park_code(self):
        test_json = ('{ "total": "2", "data": [{ "fullName": "Test Park", "parkCode":"cOdE" },'
                     '{ "fullName": "Test Park 2", "parkCode":"cOdEtWo" } ] }')
        expected = 'cOdE'
        actual = self._sut.get_park_code_from_parks_json(json.loads(test_json), 'Test Park')
        self.assertEqual(expected, actual)

    def test_given_park_amenity_json_convert_park_amenities_json_to_list_returns_correct_list(self):
        test_json = ('{ "data": [ [{ "name": "amen1", "parks": [{ "places":[ { "title": "amenity title 1" }, { "title": "amenity title 2" }] }] }] ] }')
        expected = [NationalParkAmenity('amen1', ['amenity title 1', 'amenity title 2'])]
        actual = self._sut.convert_park_amenities_json_to_list(json.loads(test_json))
        self.assertEqual(expected[0].name, actual[0].name)
        self.assertEqual(expected[0].locations_available[0], actual[0].locations_available[0])


if __name__ == '__main__':
    unittest.main()
