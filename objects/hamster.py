from . four_paws import Four_paws

class Hamster(Four_paws):
    def __init__(self, size, breed, temperament):
        super().__init__(size, breed, temperament)