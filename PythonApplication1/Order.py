from customer import Customer
from location import Location
from order_status import OrderStatus

class Order:
    def __init__(self, id, packages, paid, price, receiver, sender, status, location):
        self.id = id
        self.packages = packages
        self.paid = paid
        self.price = price
        self.receiver = receiver
        self.sender = sender
        self.status = status
        self.location = location

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def packages(self):
        return self._packages

    @packages.setter
    def packages(self, packages):
        self._packages = packages

    @property
    def paid(self):
        return self._paid

    @paid.setter
    def paid(self, paid):
        self._paid = paid

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        self._receiver = receiver

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    def __str__(self):
        return f"Order: id={self.id}, packages={self.packages}, paid={self.paid}, price={self.price}, receiver={self.receiver}, sender={self.sender}, status={self.status}, location={self.location}"
