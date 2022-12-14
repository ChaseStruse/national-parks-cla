import requests
from src.services.data_conversion_service import DataConversionService


class ApiService:
    def __init__(self, api_key, data_conversion_service=DataConversionService()):
        self.baseurl = 'https://developer.nps.gov/api/v1'
        self.api_key = api_key
        self.data_conversion_service = data_conversion_service

    def get_parks_by_state(self, state_code):
        url = self.baseurl + f'/parks?limit=5&stateCode={state_code}&api_key={self.api_key}'
        response = requests.get(url)
        return self.data_conversion_service.convert_parks_json_to_name_description_dict(response.json())

    def get_park_by_name_and_state(self, state_code, park_name):
        park_name_url = park_name.replace(' ', '%20')
        url = self.baseurl + f'/parks?limit=5&stateCode={state_code}&q={park_name_url}&api_key={self.api_key}'
        response = requests.get(url)
        return self.data_conversion_service.convert_parks_json_to_national_park_object(response.json(), park_name)

    def get_parks_amenities_by_park_name_and_state(self, state_code, park_name):
        park_name_url = park_name.replace(' ', '%20')
        url = self.baseurl + f'/parks?limit=5&stateCode={state_code}&q={park_name_url}&api_key={self.api_key}'
        response = requests.get(url)
        park_code = self.data_conversion_service.get_park_code_from_parks_json(response.json(), park_name)
        amen_url = self.baseurl + f'/amenities/parksplaces?parkCode={park_code}&api_key={self.api_key}'
        amen_response = requests.get(amen_url)
        return self.data_conversion_service.convert_park_amenities_json_to_list(amen_response.json())





