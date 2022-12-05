class NationalPark(object):
    def __init__(self, value_name='', value_description='', value_activities=None):
        if value_activities is None:
            self._activities = []
        self._name = value_name
        self._description = value_description
        self._activities = value_activities

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def activities(self):
        return self._activities

    @activities.setter
    def activities(self, value):
        self._activities = value

