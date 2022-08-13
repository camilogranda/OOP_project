from . pet import Pet

class Four_paws(Pet):
    def __init__(self, size, breed, temperament):
        super().__init__(size)

        self.breed = breed
        self.temperament = temperament
