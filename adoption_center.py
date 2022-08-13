from . account import Account

class adoption_center(Account):
    def __init__(self, name, document, email, phone):
        super().__init__(name, document, email)

        self.phone = phone

    def eval_requirements(response):
        money = input('Do you have the resources to take care of a pet?: ', response)
        ambient = input('The pet will have adequate space to be comfortable?', response)
        if money and ambient:
            print('Congratulartions! You can adopt a pet.')
        else:
            print('We\'re sorry. You don\'t meet the requirements to adopt a pet.')