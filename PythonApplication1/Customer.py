from person import Person
from bank_account import BankAccount
from credit_card import CreditCard
from location import Location
from person_type import PersonType

class Customer(Person):
    def __init__(self, invoices, shipping, creditCards, id, nationalId, idType, name, email, lastName, location, personType):
        super().__init__(id, nationalId, idType, name, email, lastName, location, personType)
        self.invoices = invoices
        self.shipping = shipping
        self.creditCards = creditCards

    @property
    def invoices(self):
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        self._invoices = invoices

    @property
    def shipping(self):
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        self._shipping = shipping

    @property
    def creditCards(self):
        return self._creditCards

    @creditCards.setter
    def creditCards(self, creditCards):
        self._creditCards = creditCards

    def __str__(self):
        return f"Customer: invoices={self.invoices}, shipping={self.shipping}, creditCards={self.creditCards}"

    def biometricValidation(self):
        return super().biometricValidation()
