class Animal():
    def __init__(self,species):
        self.species=species
    def show_species(self):
        print(f"I'm a - {self.species}")
    def sound(self):
        print(f"Grrrr!")
class Dog(Animal):
    def __init__(self):
        self.species="dog"
    def sound(self):
       print('Woof! Woof! Woof!')
class Cat(Animal):
    def __init__(self):
        self.species="cat"
    def sound(self):
        print("Meow!")
def show_animal_info(animal):
        animal.sound()
        animal.show_species()
animal=str(input("Введите вид животного: "))
if animal=="ordinary animal" or animal=="animal":
    a1=Animal(animal)
    show_animal_info(a1)
elif animal=="dog":
    animal=Dog()
    a2=show_animal_info(animal)
elif animal=="cat":
    animal=Cat()
    a2=show_animal_info(animal)
else:
    print(f"{animal} не животное")
