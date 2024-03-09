from abc import ABC, abstractmethod
from customer import Customer

class Package(ABC):
    def __init__(self, id, description, code, gramsPrice, basePrice, weight, customer):
        self.id = id
        self.description = description
        self.code = code
        self.gramsPrice = 1000 * gramsPrice
        self.basePrice = basePrice
        self.weight = weight
        self.customer = customer

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def gramsPrice(self):
        return self._gramsPrice

    @gramsPrice.setter
    def gramsPrice(self, gramsPrice):
        self._gramsPrice = gramsPrice

    @property
    def basePrice(self):
        return self._basePrice

    @basePrice.setter
    def basePrice(self, basePrice):
        self._basePrice = basePrice

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    def __str__(self):
        return f"Package: id={self.id}, description={self.description}, code={self.code}, gramsPrice={self.gramsPrice}, basePrice={self.basePrice}, weight={self.weight}, customer={self.customer}"

    def calculate(self, a, b):
        return a * b
