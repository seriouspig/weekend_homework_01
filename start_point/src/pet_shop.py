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

# Remove pet by name
def remove_pet_by_name(list, pet_name):
    pet_index = None 
    for pet in list["pets"]:
        if pet["name"] == pet_name:
            pet_index = list["pets"].index(pet)
    list["pets"].pop(pet_index)    
    
# Add pet to stock
def add_pet_to_stock(list, new_pet):
    list["pets"].append(new_pet)

# Check customer cash 
def get_customer_cash(customers):
    customer_cash = customers["cash"]
    return customer_cash

# Remove from customer cash
def remove_customer_cash(customers, cash_to_remove):
    customers["cash"] -= cash_to_remove

# Customer pet count
def get_customer_pet_count(customers):
    customer_pet_count = len(customers["pets"])
    return customer_pet_count

# Add pet to customer
def add_pet_to_customer (customer, new_pet):
    customer["pets"].append(new_pet)


