from . account import Account

class Adopter(Account):
    def __init__(self, name, document, email):
        super().__init__(name, document, email)