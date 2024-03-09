class Location:
    def __init__(self, country, state, city, addressLine1, addressLine2, zipCode):
        self.country = country
        self.state = state
        self.city = city
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.zipCode = zipCode

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def addressLine1(self):
        return self._addressLine1

    @addressLine1.setter
    def addressLine1(self, addressLine1):
        self._addressLine1 = addressLine1

    @property
    def addressLine2(self):
        return self._addressLine2

    @addressLine2.setter
    def addressLine2(self, addressLine2):
        self._addressLine2 = addressLine2

    @property
    def zipCode(self):
        return self._zipCode

    @zipCode.setter
    def zipCode(self, zipCode):
        self._zipCode = zipCode

    def __str__(self):
        return f"Location: country={self.country}, state={self.state}, city={self.city}, addressLine1={self.addressLine1}, addressLine2={self.addressLine2}, zipCode={self.zipCode}"
