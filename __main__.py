from objects.adopter import Adopter
from objects.cat import Cat
# from .objects.four_paws import Four_paws
# from objects.account import Account

def main():
    pass

adopter1 = Adopter('Carlos', 23452123, 'carlos@mail.com')
print('Information of adopter 1:')
print(adopter1.name)
print(adopter1.document)
print(adopter1.email)

print()

cat1 = Cat('Small', 'Persian', 'Agressive')
print('Information of cat 1:')
print(cat1.size)
print(cat1.breed)
print(cat1.temperament)

if __name__ == "__main__":
    main()