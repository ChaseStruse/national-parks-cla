from src.classes.national_park import NationalPark


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
