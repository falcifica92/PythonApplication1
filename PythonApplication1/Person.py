from abc import ABC, abstractmethod
from location import Location
from person_type import PersonType

class Person(ABC):
    def __init__(self, id, nationalId, idType, name, email, lastName, location, personType):
        self.id = id
        self.nationalId = nationalId
        self.idType = idType
        self.name = name
        self.email = email
        self.lastName = lastName
        self.location = location
        self.personType = personType

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nationalId(self):
        return self._nationalId

    @nationalId.setter
    def nationalId(self, nationalId):
        self._nationalId = nationalId

    @property
    def idType(self):
        return self._idType

    @idType.setter
    def idType(self, idType):
        self._idType = idType

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def personType(self):
        return self._personType

    @personType.setter
    def personType(self, personType):
        self._personType = personType

    def __str__(self):
        return f"Person: id={self.id}, nationalId={self.nationalId}, idType={self.idType}, name={self.name}, email={self.email}, lastName={self.lastName}, location={self.location}, personType={self.personType}"

    @abstractmethod
    def biometricValidation(self):
        validated = False
        return validated
