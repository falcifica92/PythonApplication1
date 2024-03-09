from datetime import date

class CreditCard:
    def __init__(self, cvv, expiryYear, expiryMonth, number, zipCode, expiryDate):
        self.cvv = cvv
        self.expiryYear = expiryYear
        self.expiryMonth = expiryMonth
        self.number = number
        self.zipCode = zipCode
        self.expiryDate = expiryDate

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        self._cvv = cvv

    @property
    def expiryYear(self):
        return self._expiryYear

    @expiryYear.setter
    def expiryYear(self, expiryYear):
        self._expiryYear = expiryYear

    @property
    def expiryMonth(self):
        return self._expiryMonth

    @expiryMonth.setter
    def expiryMonth(self, expiryMonth):
        self._expiryMonth = expiryMonth

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def zipCode(self):
        return self._zipCode

    @zipCode.setter
    def zipCode(self, zipCode):
        self._zipCode = zipCode

    @property
    def expiryDate(self):
        return self._expiryDate

    @expiryDate.setter
    def expiryDate(self, expiryDate):
        self._expiryDate = expiryDate

    def __str__(self):
        return f"CreditCard: cvv={self.cvv}, expiryYear={self.expiryYear}, expiryMonth={self.expiryMonth}, number={self.number}, zipCode={self.zipCode}, expiryDate={self.expiryDate}"

    def validation(self):
        validation = False
        return validation
