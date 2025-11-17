"""
Program data structure begins here
"""


class Meal:
    """
    Meal class
    """

    def __init__(self, name, contains, recipe, ingredients):
        self.name = name
        self.contains = contains
        self.recipe = recipe
        self.ingredients = ingredients

    def meal_info(self):
        return (
            f"Name: {self.name}, "
            f"Contains: {self.contains}, "
            f" Recipe link: {self.recipe}, "
            f" Ingredients: {self.ingredients}"
        )


"""
Objects with Meal class
"""
FishAndChips = Meal(
    "Fish and Chips", "fish", "www.bbcgoodfood.com", ["fish", "chips", "peas"]
)

SausageAndMash = Meal(
    "Sausage and Mash", "meat", "www.bbcgoodfood.com", ["sausage", "potato"]
)

ChickenCurry = Meal(
    "Chicken Curry and Rice",
    "meat",
    "www.bbcgoodfood.com",
    ["chicken", "jar of curry sauce", "rice"],
)

SpagBol = Meal(
    "Spaghetti Bolognese",
    ["meat", "wheat"],
    "www.bbcgoodfood.com",
    ["mince", "jar of bolognese sauce", "spaghetti"],
)

Gnocchi = Meal(
    "Gnocchi with Pesto",
    "wheat",
    "www.bbcgoodfood.com",
    ["gnocchi", "jar of pesto"]
)

BeanChilli = Meal(
    "Bean Chilli with Rice",
    "",
    "www.bbcgoodfood.com",
    ["tinned beans", "jar of chilli sauce", "rice"],
)

Seabass = Meal(
    "Seabass with New Potatoes",
    "fish",
    "www.bbcgoodfood.com",
    ["seabass fillet", "new potatoes", "lemon"],
)

Penne = Meal(
    "Penne with Vodka Tomato Sauce",
    "wheat",
    "www.bbcgoodfood.com",
    ["penne pasta", "tinned tomato", "vodka"],
)

Lasagne = Meal(
    "Roast Veg Lasagne",
    "wheat",
    "www.bbcgoodfood.com",
    ["lasagne sheets", "summer vegetables", "tinned tomato", "mozarella"],
)

FishPie = Meal(
    "Fish Pie",
    "fish",
    "www.bbcgoodfood.com",
    ["frozen fish pie mix", "baking potato", "milk", "flour"],
)

ChickpeaStew = Meal(
    "Chickpea Stew",
    "",
    "www.bbcgoodfood.com",
    ["tinned chickpea", "coconut milk", "onions", "garlic"],
)

LentilCurry = Meal(
    "Lentil Curry and Rice",
    "",
    "www.bbcgoodfood.com",
    ["dried lentils", "Madras curry powder", "onions", "garlic", "rice"],
)

StirFry = Meal(
    "Stir-fried Veg Noodles",
    "wheat",
    "www.bbcgoodfood.com",
    ["bag stir fry veg", "noodles", "soy sauce"],
)

Tacos = Meal(
    "Jackfruit Tacos",
    "wheat",
    "www.bbcgoodfood.com",
    ["tinned jackfruit", "sour cream", "tacos", "jar of salsa"],
)

BakedPotato = Meal(
    "Baked Potato with Beans and Cheese",
    "",
    "www.bbcgoodfood.com",
    ["baking potato", "tin of baked beans", "Cheddar cheese"],
)

Risotto = Meal(
    "Mushroom Risotto",
    "",
    "www.bbcgoodfood.com",
    ["risotto rice", "mushroom", "parmesan"],
)

ShepherdsPie = Meal(
    "Shepherd's Pie",
    "meat",
    "www.bbcgoodfood.com",
    ["lamb mince", "onions", "baking potato", "tinned tomato"],
)

Stroganoff = Meal(
    "Mushroom Stroganoff and Rice",
    "",
    "www.bbcgoodfood.com",
    ["mushroom", "cream", "paprika", "rice"],
)

Cheeseburger = Meal(
    "Cheeseburger and Fries",
    ["meat", "wheat"],
    "www.bbcgoodfood.com",
    ["burger patties", "burger buns", "pickles", "American cheese", "fries"],
)

Pie = Meal(
    "Chicken Pie and Mash",
    ["meat", "wheat"],
    "www.bbcgoodfood.com",
    [
        "chicken thighs",
        "milk",
        "flour",
        "butter",
        "leeks",
        "puff pastry",
        "baking potato",
    ],
)

ThaiCurry = Meal(
    "Thai Green Curry with Rice",
    "",
    "www.bbcgoodfood.com",
    [
        "tofu",
        "carrots",
        "red pepper",
        "coconut milk",
        "Thai Green Curry Paste",
        "jasmine rice",
    ],
)

meal_list = [
    FishAndChips,
    SausageAndMash,
    ChickenCurry,
    SpagBol,
    Gnocchi,
    BeanChilli,
    Seabass,
    Penne,
    Lasagne,
    FishPie,
    ChickpeaStew,
    LentilCurry,
    StirFry,
    Tacos,
    BakedPotato,
    Risotto,
    ShepherdsPie,
    Stroganoff,
    Cheeseburger,
    Pie,
    ThaiCurry
]


"""
Data structure ends here
"""

"""
Functions
"""


def return_random_meals():
    import random

    random_meals = random.sample(meal_list, 7)
    print("Here are your week's evening meals:\n")

    print(f"Monday - {random_meals[0].name}")
    print(f"Tuesday - {random_meals[1].name}")
    print(f"Wednesday - {random_meals[2].name}")
    print(f"Thursday - {random_meals[3].name}")
    print(f"Friday - {random_meals[4].name}")
    print(f"Saturday - {random_meals[5].name}")
    print(f"Sunday - {random_meals[6].name}\n")

    sample_response = (input(
        "If you are happy with your selection, "
        "please press 'enter' to continue. "
        "If you would like to see a different meal plan, "
        "please press any other key and then 'enter':")
    )
    if sample_response == "":
        print("We're glad you like your Evening Meal Plan!\n")
        create_shopping_list(random_meals)

    else:
        return_random_meals()


def create_shopping_list(random_meals):
    print("Here is your shopping list for the week:\n")
    shopping_list = []
    for meal in random_meals:
        for ingredient in meal.ingredients:
            shopping_list.append(ingredient)

    print(shopping_list)


print("Welcome to your Evening Meal Planner!\n")
return_random_meals()
