import os
from services.api_service import ApiService
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('API_KEY')
api_service = ApiService(key)

if __name__ == '__main__':
    name_description_dict = api_service.get_parks_by_state('CA')
    for key, value in name_description_dict.items():
        print(f'{key} \n{value} \n')
