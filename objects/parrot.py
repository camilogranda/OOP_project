from . birds import Birds

class Parrot(Birds):
    def __init__(self, size, species):
        super().__init__(size, species)