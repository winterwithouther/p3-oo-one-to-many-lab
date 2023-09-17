class Pet:

    all = []
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def get_pet_type(self):
        return self._pet_type
    
    def set_pet_type(self, new_pet_type):
        if new_pet_type in Pet.PET_TYPES:
            self._pet_type = new_pet_type
            return self._pet_type
        else:
            raise Exception("Object is not of type Owner")
        
    pet_type = property(get_pet_type, set_pet_type)

    

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Input object is not of type Pet")

    def get_sorted_pets(self):
        def get_pet_name(pet):
            return pet.name
        
        return sorted(self.pets(), key=get_pet_name)

mr_kim = Owner("Mr. Kim")
mr_jim = Owner("Mr. Jim")
cat = Pet("meowsir", "cat", mr_kim)
dog = Pet("buddy", "dog", mr_kim)
rat = Pet("hammy", "rodent")
print(mr_kim.pets())
print(mr_kim.get_sorted_pets())