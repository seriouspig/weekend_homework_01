pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }



# def get_pets_by_breed(list, breed_name):

#     pets_by_breed = []

#     for pet in list["pets"]:
#         if list["pets"][0]["breed"] == breed_name:
#             pets_by_breed.append(1)
#     return pets_by_breed
#     print(pets_by_breed)

# get_pets_by_breed(pet_shop, "Husky")

# print (pet_shop["pets"][5])

def remove_pet_by_name(list, pet_name):
    pet_index = None 
    for pet in list["pets"]:
        if pet["name"] == pet_name:
            pet_index = list["pets"].index(pet)
            
    print(pet_index)    

remove_pet_by_name(pet_shop, "Arthur")