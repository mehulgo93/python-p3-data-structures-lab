spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_food_names = []

    # Iterate through each item in the list of spicy foods
    for spicy_food in spicy_foods:
        # Check if the item is a dictionary and contains the 'name' key
        if isinstance(spicy_food, dict) and 'name' in spicy_food:
            # Append the name of the spicy food to the list
            spicy_food_names.append(spicy_food['name'])
    return spicy_food_names

def get_spiciest_foods(spicy_foods):
   spiciest_foods = []
   for food in spicy_foods:
       if food.get("heat_level") > 5:
           spiciest_foods.append(food)
       return spiciest_foods
       
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name", "unknown")
        cuisine = food.get("cuisine", "unknown")
        heat_level = food.get("heat_level", 0)
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine", "") == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
         name = food.get("name", "unknown")
         cuisine = food.get("cuisine", "unknown")
         heat_level = food.get("heat_level", 0)
         heat_emojis = "🌶" * heat_level
         if heat_level > 5:
             print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")
             

def get_average_heat_level(spicy_foods):

    # Calculate the total heat level by summing all the heat levels
           total_heat_level = sum(food["heat_level"] for food in spicy_foods)

    # Calculate the average heat level by dividing the total by the number of elements
           average_heat = total_heat_level / len(spicy_foods)

    # Return the average heat level
           return average_heat



def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods




