import os
from services.api_service import ApiService
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('API_KEY')
api_service = ApiService(key)


def print_command_menu():
    print('Please select from the list of commands below: \n')
    print('1. Get parks in your state')
    print('2. Get park and activities (Requires park name and state abbreviation)')
    print('3. Get parks amenities (Requires park name and state abbreviation)')
    print('4. ')


def print_parks_and_descriptions():
    state_abbrev = input('Please enter state abbreviation(ex: CA): ')
    try:
        name_description_dict = api_service.get_parks_by_state(state_abbrev)

        print('____________________________')
        print('\nList of National Parks')
        print('____________________________')
        for park, description in name_description_dict.items():
            print(f'{park} \n{description} \n')
        input('Press enter to continue')
    except:
        print('Please check input and try again \n')
        print_parks_and_descriptions()


def print_park_information():
    try:
        state_abbrev = input('Please enter state abbreviation(ex: CA): ')
        park_name = input('Please enter park name: ')
        park = api_service.get_park_by_name_and_state(state_abbrev, park_name)

        print('____________________________')
        print('Park Information')
        print('____________________________')
        print(f'{park.name} \n'
              f'{park.description} \n')
        print('List of Activities Available')
        print('____________________________')
        print(*park.activities, sep=', ')
        print('____________________________\n')
        input('Press enter to continue')
    except:
        print('Please check input and try again \n')
        print_park_information()


def print_park_amenities():
    try:
        state_abbrev = input('Please enter state abbreviation(ex: CA): ')
        park_name = input('Please enter park name: ')
        amenities = api_service.get_parks_amenities_by_park_name_and_state(state_abbrev, park_name)

        print('___________________________')
        for amenity in amenities:
            print(f'Amenity: {amenity.name}\n')
            print(*amenity.locations_available, ', ')
            print('___________________________')
        input('Press enter to continue')
    except ValueError:
        print('Please check input and try again \n')
        print_park_amenities()


def main_loop():
    keep_using = True
    print('Welcome to National Parks Command Line Application \n')
    print('__________________________________________________')
    while keep_using:
        try:
            print_command_menu()
            selection = int(input('Enter selection: '))

            if selection == 1:
                print_parks_and_descriptions()

            elif selection == 2:
                print_park_information()

            elif selection == 3:
                print_park_amenities()

            elif selection == 0:
                print('Thank you for using the application!')
                keep_using = False

        except ValueError:
            print('Please ensure you are entering a number from the menu \n')


if __name__ == '__main__':
    main_loop()
