# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/21/2023
# Description: reads a JSON file to record neighborhood pets

import json

class DuplicateNameError(Exception):
    """exception error"""
    pass

class NeighborhoodPets:
    """create neighborhoodpets class"""
    def __init__(self):
        self.__pets = []        # creat a list

    def add_pet(self, name, species, owner):
        """add pet method"""
        for pet in self.__pets:
            if pet["name"] == name:     
                raise DuplicateNameError("Pet with the same name already exists.")      # raise the error I create
        
        pet_data = {
            "name": name,
            "species": species,
            "owner": owner
        }
        self.__pets.append(pet_data)        # append to pet data

    def delete_pet(self, name):
        """delete pet name method"""
        if name in self.__pets:     # check if the name is already exist
            del self.__pets[name]       # delete

    def get_owner(self, name):
        """get owner method"""
        for pet in self.__pets:
            if pet["name"] == name:     # check if the pet is exist
                return pet["owner"]     # return owner name
        return None

    def save_as_json(self, file_name):
        """save as .json file"""
        with open(file_name, 'w') as file:      # open and write
            json.dump(self.__pets, file)        # use .dump()

    def read_json(self, file_name):
        """read .json file"""
        with open(file_name, 'r') as file:      # open and read
            self.__pets = json.load(file)       # use .load()

    def get_all_species(self):
        """get all species method"""
        return {pet["species"] for pet in self.__pets}      # return all species

"""Example"""
# def main():
np = NeighborhoodPets()
try:
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegosaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
except DuplicateNameError:
    print('You tried to enter a pet with the same name as another pet.')

np.save_as_json("pets.json")
np.delete_pet("Tiny")
spot_owner = np.get_owner("Spot")
np.read_json("pets.json")  
species_set = np.get_all_species()

# if __name__ == '__main__':
#     main()