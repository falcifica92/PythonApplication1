from customer import Customer
from location import Location
from invoice_status import InvoiceStatus
from payment_methods_types import PaymentMethodsTypes

class Invoice:
    def __init__(self, id, tax, price, discount, orders, status, client, paymentMethod):
        self.id = id
        self.tax = tax
        self.price = price
        self.discount = discount
        self.orders = orders
        self.status = status
        self.client = client
        self.paymentMethod = paymentMethod

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, tax):
        self._tax = tax

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, orders):
        self._orders = orders

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def paymentMethod(self):
        return self._paymentMethod

    @paymentMethod.setter
    def paymentMethod(self, paymentMethod):
        self._paymentMethod = paymentMethod

    def __str__(self):
        return f"Invoice: id={self.id}, tax={self.tax}, price={self.price}, discount={self.discount}, orders={self.orders}, status={self.status}, client={self.client}, paymentMethod={self.paymentMethod}"
