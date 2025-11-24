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
            f"Name: {self.name},\n"
            f"Contains: {self.contains},\n"
            f"Recipe link: {self.recipe},\n"
            f"Ingredients: {self.ingredients}\n"
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
        "please press any other key and then 'enter':\n")
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
    print("")

    show_recipes(random_meals)


def show_recipes(random_meals):
    recipe_response = (input(
        "If you would like to see links to recipes, "
        "please press 'enter'."
        "If you don't require recipes, "
        "please press any other key and then 'enter' to continue:\n")
    )
    if recipe_response == "":
        print("Here are some recipe links for your meal plan\n")
        for meal in random_meals:
            print(f"{meal.name} - {meal.recipe}")
            print("")
        personal_meals_request()

    else:
        personal_meals_request()


def personal_meals_request():
    personalise_response = input(
        "To customise your experience,"
        "would you like to add your own meals to the Meal Planner?"
        "If yes, please press 'enter'."
        "If no, please press any other key and then 'enter' to continue:\n"
    )

    if personalise_response == "":
        add_personal_meal()
    else:
        ending_function()


def add_personal_meal():

    new_name = input("Please enter the name of your meal:\n")
    new_contains = input("Please enter any ingredients, separated with commas,"
                         "that users may dislike or be allergic to:\n")
    new_recipe = input("Please enter a link to the recipe for your meal:\n")
    new_ingredients = input("Please enter the ingredients for your meal,"
                            "separated with commas:\n")
    NewMeal = (Meal(new_name, new_contains, new_recipe, new_ingredients))
    meal_list.append(NewMeal)

    print("")
    print("Thank you, you have added:\n")
    print(Meal.meal_info(NewMeal))

    add_another_meal_response = input(
        "Would you like to add another meal to the Meal Planner?\n"
        "If yes, please press 'enter'.\n"
        "If no, please press any other key and then 'enter' to continue:\n"
    )

    if add_another_meal_response == "":
        add_personal_meal()
    else:
        restart_program_response = input(
            "Would you like to see a new meal plan?\n"
            "If yes, please press 'enter'"
            "To exit the program, press any key, followed by 'enter'"
        )

        if restart_program_response == "":
            return_random_meals()
        else:
            ending_function()


def ending_function():
    print("Thanks for using the Evening Meal Planner\n")


print("Welcome to your Evening Meal Planner!\n")
return_random_meals()
