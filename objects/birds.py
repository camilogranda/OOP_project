from . pet import Pet

class Bird(Pet):
    def __init__(self, size, species):
        super().__init__(size)

        self.species = species