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
    names = [x['name'] for x in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    heat_greater_than_five = [heat for heat in spicy_foods if heat['heat_level'] > 5]
    return heat_greater_than_five

def print_spicy_foods(spicy_foods):
    return [print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}') for food in spicy_foods]   

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    return [(print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")) for food in spicy_foods if food['heat_level'] > 5] 
            

def get_average_heat_level(spicy_foods):
    total_sum = sum(food['heat_level'] for food in spicy_foods)

    average = total_sum / len(spicy_foods)

    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods