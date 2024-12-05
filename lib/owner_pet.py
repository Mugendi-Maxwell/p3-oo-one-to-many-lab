class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string.")
        self.name = name
        self._pets = []  

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        if pet not in self._pets:
            self._pets.append(pet)
            pet.owner = self  

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    def __str__(self):
        return self.name


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string.")
        if not isinstance(pet_type, str):
            raise Exception("Pet type must be a string.")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Allowed types are: {', '.join(Pet.PET_TYPES)}.")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class or None.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)  
        Pet.all.append(self)  

    def __str__(self):
        if self.owner:
            return f"{self.name} is a {self.pet_type} owned by {self.owner.name}."
        else:
            return f"{self.name} is a {self.pet_type} with no owner."
