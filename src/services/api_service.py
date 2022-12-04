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
        park = self.data_conversion_service.convert_parks_json_to_name_description_dict(response.json())
        return park




