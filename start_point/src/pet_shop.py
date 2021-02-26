# WRITE YOUR FUNCTIONS HERE

# Pet shop name
def get_pet_shop_name(list):
    return list["name"]



# Total cash
def get_total_cash(list):
    return list["admin"]["total_cash"]

# Add or remove cash
def add_or_remove_cash(list, add_amount):
    list["admin"]["total_cash"] += add_amount


# Pets sold
def get_pets_sold(list):
    return list["admin"]["pets_sold"]

# Increase pets sold
def increase_pets_sold(list,pets_sold_amount):
    list["admin"]["pets_sold"] += pets_sold_amount

# Stock count
def get_stock_count(list):
    return len(list["pets"])

# Get pets by breed
def get_pets_by_breed(list, breed_name):
    pets_by_breed = []
    for pet in list["pets"]:
        if pet["breed"] == breed_name:
            pets_by_breed.append(1)
    return pets_by_breed

# Find pet by name
def find_pet_by_name(list, pet_name):
    pet_by_name = None
    for pet in list["pets"]:
        if pet["name"] == pet_name:
            pet_by_name = pet
    return pet_by_name