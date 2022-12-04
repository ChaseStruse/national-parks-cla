
class DataConversionService:
    @staticmethod
    def convert_parks_json_to_name_description_dict(json):
        data = json['data']
        name_description = {state['fullName']: state['description'] for state in data}
        return name_description
