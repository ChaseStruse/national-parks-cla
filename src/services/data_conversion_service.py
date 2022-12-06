from src.classes.national_park import NationalPark
from src.classes.national_park_amenity import NationalParkAmenity


class DataConversionService:
    @staticmethod
    def convert_parks_json_to_name_description_dict(json):
        data = json['data']
        name_description = {state['fullName']: state['description'] for state in data}
        return name_description

    @staticmethod
    def convert_parks_json_to_national_park_object(json, park_name):
        total_responses = int(json['total'])
        data = json['data']
        park = NationalPark()

        if total_responses == 1:
            park.name = data[0]['fullName']
            park.description = data[0]['description']
            park.activities = [act['name'] for act in data[0]['activities']]

        elif total_responses > 1:
            for park_info in data:
                if park_info['fullName'] == park_name:
                    park.name = park_info['fullName']
                    park.description = park_info['description']
                    park.activities = [act['name'] for act in park_info['activities']]

        return park

    @staticmethod
    def convert_park_amenities_json_to_list(json):
        data = json['data']
        list_of_amenities = []

        for amenity in data:
            name = amenity[0]['name']
            locations = []
            for park in amenity[0]['parks'][0]['places']:
                locations.append(park['title'])
            list_of_amenities.append(NationalParkAmenity(name, locations))
        return list_of_amenities

    @staticmethod
    def get_park_code_from_parks_json(json, park_name):
        total_responses = int(json['total'])
        data = json['data']
        park_code = ''

        if total_responses == 1:
            park_code = data[0]['parkCode']

        elif total_responses > 1:
            for park_info in data:
                if park_info['fullName'] == park_name:
                    park_code = park_info['parkCode']

        return park_code



