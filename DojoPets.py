class Pet:
    pet_list = []
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        Pet.pet_list.append(name)
        print(f"Pet Type Added!: {self.type}")
        return
    def sleep(name):
        name.energy += 25
        print(f"{name}, has gained 25 energy points.")
        print(f"{name}, now has {name.energy} energy!")
        return 
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} Has been fed!")
        print(f"Energy:{self.energy}")
        print(f"Health:{self.health}")
        return
    def play(self):
        self.health += 5
        print(f"{self.name} had so much fun, what a workout!")
        print(f"Health: {self.health}")
    def noise(self):
        if self.type == "Dog":
            print(f"{self.name}: Bark! Bark!")
        else:
            print(f"What does {self.name} sound like? Pet unrecongized!")
            return
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet): 
        self.first_name = first_name 
        self.last_name = last_name 
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        self.pet = Pet(name=pet, type="Dog", tricks=["Fetch", "Rollover"], health= 50, energy= 50)
        print(pet)
        print(f"Owner:{first_name}" )
        return
    def walk(self, pet):
        print(f"{self.first_name} took {pet} for a walk.")
        Pet.play(self.pet)
    def feed(self, pet):
        print(f"{self.first_name} fed {self.treats} to {pet}")
        Pet.eat(self.pet)
    def bathe(self, pet):
        print(f"{self.first_name} hosed down {pet}")
        Pet.noise(self.pet)

alonzo = Ninja(" alonzo", "madrid", "Dog Bone", "bowls" == 5, "Chester")
alonzo.feed("Chester")
alonzo.walk("Chester")
alonzo.bathe("Chester")