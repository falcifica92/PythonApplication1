from customer import Customer
from location import Location
from order import Order
from invoice import Invoice
from standard_package import StandardPackage
from person_type import PersonType
from order_status import OrderStatus
from invoice_status import InvoiceStatus
from payment_methods_types import PaymentMethodsTypes

num = 100
orders = [None]*num
invoices = [None]*num
locations = [None]*num

def menu():
    opcion = 0

    while opcion != 2:
        print("\n\t.:MENU:.")
        print("1. Enviar un paquete")
        print("2. Salir")
        opcion = int(input("Digite una opcion: "))

        if opcion == 1:
            print("")
            send_package()
        elif opcion == 2:
            print("Haz salido del menu\n")
        else:
            print("Opcion incorrecta\n")

def send_package():
    pack = None
    a = input("Ingresar los datos del remitente: \nIdentificacion: ")
    b = input("Nacionalidad: ")
    c = input("Nombre: ")
    d = input("Apellido: ")
    e = input("Email: ")

    print("Ingresar la direccion del remitente: ")
    f = input("Pais: ")
    g = input("Departamento: ")
    h = input("Ciudad: ")
    i = input("Calle: ")
    j = input("Carrera: ")
    k = int(input("Codigo postal: "))

    dir_a = Location(f, g, h, i, j, k)
    locations[0] = dir_a
    user_a = Customer(None, locations[0], None, a, b, "CC", c, e, d, dir_a, PersonType.LEGAL)

    a = input("Ingresar los datos del Destinatario: \nIdentificacion: ")
    b = input("Nacionalidad: ")
    c = input("Nombre: ")
    d = input("Apellido: ")
    e = input("Email: ")

    print("Ingresar la direccion del Destinatario: ")
    f = input("Pais: ")
    g = input("Departamento: ")
    h = input("Ciudad: ")
    i = input("Calle: ")
    j = input("Carrera: ")
    k = int(input("Codigo postal: "))

    dir_b = Location(f, g, h, i, j, k)
    locations[1] = dir_b
    user_b = Customer(None, locations[1], None, a, b, "CC", c, e, d, dir_b, PersonType.LEGAL)

    pack = StandardPackage(5500, "E0001", "Chancletas", 003145, 7.5, 10000, 2.5, user_a)
    TotalPagar = pack.calculate(pack.getGramsPrice(), pack.getWeight(), pack.getQuota())

    orders[0] = Order("Or0001", pack, True, TotalPagar, user_b, user_a, OrderStatus.PENDING, locations[0])

    invoices[0] = Invoice("Inv0001", 0, TotalPagar, 0, orders[0], InvoiceStatus.SENT, user_a, PaymentMethodsTypes.CASH)

    user_a.setInvoices(invoices[0])
    user_b.setInvoices(invoices[0])

    print("\n\tDATOS DEL REMITENTE"
        + "\nIdentidad: " + user_a.getId()
        + "\nNombre: " + user_a.getName()
        + "\nDireccion de origen: " + str(locations[0])
        + "\nDireccion de envio: " + str(locations[1])
        + "\nId Factura: " + user_a.getInvoices().getId())

    print("\n\tDATOS DEL DESTINATARIO"
        + "\nIdentidad: " + user_b.getId()
        + "\nNombre: " + user_b.getName()
        + "\nId Factura: " + user_b.getInvoices().getId())

    print("\n\tDATOS DEL PAQUETE"
        + "\nId del paquete: " + pack.getId()
        + "\nDescripcion: " + pack.getDescription()
        + "\nPeso: " + str(pack.getWeight())
        + "\nPrecio de gramo:" + str(pack.getGramsPrice())
        + "\nCuota fija: " + str(pack.getQuota()))

    print("\n\tDATOS DE LA ORDEN"
        + "\nId de la orden: " + orders[0].getId()
        + "\nId Paquete: " + orders[0].getPackages().getId()
        + "\nPago valido: " + str(orders[0].isPaid())
        + "\nId Remitente: " + orders[0].getSender().getId()
        + "\nId Destinatario: " + orders[0].getReceiver().getId())

    print("\n\tDATOS DE LA FACTURA"
        + "\nId de la factura: " + invoices[0].getId()
        + "\nId de la orden: " + invoices[0].getOrders().getId()
        + "\nEstado: " + str(invoices[0].getStatus())
        + "\nTotal a pagar: " + str(invoices[0].getPrice())
        + "\nMetodo de pago: " + str(invoices[0].getPaymentMethod()))

if __name__ == "__main__":
    menu()
