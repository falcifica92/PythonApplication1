from person import Person  # Assuming you have a Person class defined somewhere
from role import Role  # Assuming you have a Role class defined somewhere
from bank_account import BankAccount  # Assuming you have a BankAccount class defined somewhere

class Internal(Person):
    def __init__(self, role, account, id, national_id, id_type, name, email, last_name, location, person_type):
        super().__init__(id, national_id, id_type, name, email, last_name, location, person_type)
        self.role = role
        self.account = account

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        self._account = account

    def biometric_validation(self):
        return super().biometric_validation()

    def __str__(self):
        return f"Internal{{role={self.role}, account={self.account}}}"
