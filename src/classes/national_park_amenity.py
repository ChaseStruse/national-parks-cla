class NationalParkAmenity(object):
    def __init__(self, value_name='', value_locations_available=None):
        if value_locations_available is None:
            self._locations_available = []
        self._name = value_name
        self._locations_available = value_locations_available

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def locations_available(self):
        return self._locations_available

    @locations_available.setter
    def locations_available(self, value):
        self._locations_available = value
