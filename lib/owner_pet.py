class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        pets_list = []
        for pet in Pet.all:
            if pet.owner == self:
                pets_list.append(pet)
        return pets_list

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("The pet must be an instance of the Pet class")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("The owner must be an instance of the Owner class")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)
