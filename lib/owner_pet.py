class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all_pets.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.owned_pets = []

    def pets(self):
        return self.owned_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Must be a valid pet object")
        self.owned_pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.owned_pets, key=lambda x: x.name)
        return sorted_pets
