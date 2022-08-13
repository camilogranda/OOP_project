class Account:
    name = str
    document = str
    email = str

    def __init__(self, name, document, email):
        self.name = name
        self.document = document
        self.email = email