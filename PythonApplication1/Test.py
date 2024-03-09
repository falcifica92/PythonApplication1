import unittest
from customer import Customer
from location import Location
from order import Order
from invoice import Invoice
from standard_package import StandardPackage
from person_type import PersonType
from order_status import OrderStatus
from invoice_status import InvoiceStatus
from payment_methods_types import PaymentMethodsTypes

class TestTaller(unittest.TestCase):

    def setUp(self):
        self.location = Location("Pais", "Departamento", "Ciudad", "Calle", "Carrera", 12345)
        self.customer = Customer(None, self.location, None, "123456", "Nacionalidad", "CC", "Nombre", "Email", "Apellido", self.location, PersonType.LEGAL)
        self.package = StandardPackage(5500, "E0001", "Chancletas", 003145, 7.5, 10000, 2.5, self.customer)
        self.order = Order("Or0001", self.package, True, 10000, self.customer, self.customer, OrderStatus.PENDING, self.location)
        self.invoice = Invoice("Inv0001", 0, 10000, 0, self.order, InvoiceStatus.SENT, self.customer, PaymentMethodsTypes.CASH)

    def test_location(self):
        self.assertEqual(self.location.country, "Pais")


    def test_customer(self):
        self.assertEqual(self.customer.id, "123456")


    def test_package(self):
        self.assertEqual(self.package.id, "E0001")


    def test_order(self):
        self.assertEqual(self.order.id, "Or0001")


    def test_invoice(self):
        self.assertEqual(self.invoice.id, "Inv0001")


if __name__ == '__main__':
    unittest.main()
