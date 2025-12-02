import random

"""
Program data structure begins here
"""

MEAL_DATABASE = [
    {
        "name": "Fish and Chips",
        "contains": ["fish"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "next-level-fish-chips",
        "ingredients": ["fish", "chips", "peas"]
    },
    {
        "name": "Sausage and Mash",
        "contains": ["meat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "bangers-n-mash-with-onion-gravy",
        "ingredients": ["sausage", "potato"]
    },
    {
        "name": "Chicken Curry and Rice",
        "contains": ["meat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "easy-chicken-curry",
        "ingredients": [
            "chicken",
            "jar of curry sauce",
            "rice"
        ]
    },
    {
        "name": "Spaghetti Bolognese",
        "contains": ["meat", "wheat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "big-batch-bolognese",
        "ingredients": [
            "mince",
            "jar of bolognese sauce",
            "spaghetti"
        ]
    },
    {
        "name": "Gnocchi with Pesto",
        "contains": ["wheat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "gnocchi-lemon-chive-pesto",
        "ingredients": ["gnocchi", "jar of pesto"]
    },
    {
        "name": "Bean Chilli with Rice",
        "contains": [],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "vegetable-bean-chilli",
        "ingredients": [
            "tinned beans",
            "jar of chilli sauce",
            "rice"
        ]
    },
    {
        "name": "Seabass with New Potatoes",
        "contains": ["fish"],
        "recipe": "https://www.bbcgoodfood.com/"
        "search?q=seabass",
        "ingredients": [
            "seabass fillet",
            "new potatoes",
            "lemon"
        ]
    },
    {
        "name": "Penne with Vodka Tomato Sauce",
        "contains": ["wheat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "pasta-alla-vodka",
        "ingredients": [
            "penne pasta",
            "tinned tomato",
            "vodka"
        ]
    },
    {
        "name": "Roast Veg Lasagne",
        "contains": ["wheat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "five-veg-lasagne",
        "ingredients": [
            "lasagne sheets",
            "summer vegetables",
            "tinned tomato",
            "mozarella"
        ]
    },
    {
        "name": "Fish Pie",
        "contains": ["fish"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "family-meals-easy-fish-pie-recipe",
        "ingredients": [
            "frozen fish pie mix",
            "baking potato",
            "milk",
            "flour"
        ]
    },
    {
        "name": "Chickpea Stew",
        "contains": [],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "spicy-chickpea-stew",
        "ingredients": [
            "tinned chickpea",
            "coconut milk",
            "onions",
            "garlic"
        ]
    },
    {
        "name": "Lentil Curry and Rice",
        "contains": [],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "easy-peasy-lentil-curry",
        "ingredients": [
            "dried lentils",
            "Madras curry powder",
            "onions",
            "garlic",
            "rice"
        ]
    },
    {
        "name": "Stir-fried Veg Noodles",
        "contains": ["wheat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "sticky-tempeh-stir-fry",
        "ingredients": [
            "bag stir fry veg",
            "noodles",
            "soy sauce"
        ]
    },
    {
        "name": "Jackfruit Tacos",
        "contains": ["wheat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "mini-jackfruit-tacos-charred-sweetcorn-gochujang-mayo",
        "ingredients": [
            "tinned jackfruit",
            "sour cream",
            "tacos",
            "jar of salsa"
        ]
    },
    {
        "name": "Baked Potato with Beans and Cheese",
        "contains": [],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "crisp-baked-potatoes",
        "ingredients": [
            "baking potato",
            "tin of baked beans",
            "Cheddar cheese"
        ]
    },
    {
        "name": "Mushroom Risotto",
        "contains": [],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "mushroom-risotto",
        "ingredients": ["risotto rice", "mushroom", "parmesan"]
    },
    {
        "name": "Shepherd's Pie",
        "contains": ["meat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "no-fuss-shepherds-pie",
        "ingredients": [
            "lamb mince",
            "onions",
            "baking potato",
            "tinned tomato"
        ]
    },
    {
        "name": "Mushroom Stroganoff and Rice",
        "contains": [],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "no-fuss-shepherds-pie",
        "ingredients": ["mushroom", "cream", "paprika", "rice"]
    },
    {
        "name": "Cheeseburger and Fries",
        "contains": ["meat", "wheat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "cheeseburger-chips",
        "ingredients": [
            "burger patties",
            "burger buns",
            "pickles",
            "American cheese",
            "fries"
        ]
    },
    {
        "name": "Chicken Pie and Mash",
        "contains": ["meat", "wheat"],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "next-level-chicken-pie",
        "ingredients": [
            "chicken thighs",
            "milk",
            "flour",
            "butter",
            "leeks",
            "puff pastry",
            "baking potato"
        ]
    },
    {
        "name": "Thai Green Curry with Rice",
        "contains": [],
        "recipe": "https://www.bbcgoodfood.com/recipes/"
        "vegetarian-thai-green-curry",
        "ingredients": [
            "tofu",
            "carrots",
            "red pepper",
            "coconut milk",
            "Thai Green Curry Paste",
            "jasmine rice"
        ]
    }
]


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


meal_list = []
# Create meal list from database.
for item in MEAL_DATABASE:
    meal = Meal(item["name"], item["contains"],
                item["recipe"], item["ingredients"])
    meal_list.append(meal)


"""
Data structure ends here
"""

"""
Functions
"""
filtered_meal_list = []


def get_restrictions():
    """
    Get dietary restrictions from user.
    Remove meals from meal list that contain restricted ingredients,
    either in the 'contains' attribute or the 'ingredients' attribute.
    """
    print("Before we create your meal plan, "
          "let's check for any dietary restrictions, "
          "i.e. allergies or dislikes.")

    while True:
        restrictions_input = input(
            "Please enter any ingredients you would like to avoid, "
            "seperated with commas, and then press 'enter'.\n"
            "If you have no restrictions, just press 'enter':\n")
        # Check input contains only letters, spaces and commas,
        # else print error message.
        if all(char.isalpha() or char.isspace() or char == ','
               for char in restrictions_input):
            break
        else:
            print("Invalid input. Please enter letters, spaces, "
                  "and commas only.")
            continue

    if restrictions_input == "":
        print("You have entered no dietary restrictions.\n")
        filtered_meal_list.extend(meal_list)
        return_random_meals()

    else:
        # Create restrictions list, in lowercase to match database strings.
        restrictions = [item.strip().lower()
                        for item in restrictions_input.split(",")]
        print(
            f"You have entered the following dietary restrictions:"
            f"{restrictions}\n")
        # Remove meals containing restricted items in the 'contains' attribute.
        for meal in meal_list:
            should_remove = False
            for item in meal.contains:
                if item.lower() in restrictions:
                    should_remove = True
                    break
            # Remove meals containing restricted
            # items in the 'ingredients' attribute.
            if not should_remove:
                for ingredient in meal.ingredients:
                    for restriction in restrictions:
                        if restriction in ingredient.lower():
                            should_remove = True
                            break
            # Append approved meals to filtered meal list.
            if not should_remove:
                filtered_meal_list.append(meal)

        # Check filtered meal list is at least seven items long,
        # return an error message if under 7 items and request
        # user to add personal meals.
        if len(filtered_meal_list) < 7:
            print(
                "Thanks for your response.\n"
                "Please see below you new meal data base, with your "
                "restrictions taken into account:\n"
                )
            for meal in filtered_meal_list:
                print(meal.name)
                print("")
            sample_too_low()

        else:
            # Print the filtered meal list for the user.
            print("We have updated the meal options based on your reply.\n")
            print("Please see below you new meal data base, with your "
                  "restrictions taken into account"
                  )
            for meal in filtered_meal_list:
                print(meal.name)
            print("")
            input("Press 'enter' to see your Evening Meal Plan!:\n")
            return_random_meals()


def sample_too_low():
    """
    Request the user to add personal meals to the database
    to increase the filtered meal list to at least 7 items
    in length, or exit the program.
    """
    print(f"Your meal database now contains "
          f"'{len(filtered_meal_list)}' "
          f"meals! "
          f"Evening Meal Planner requires a minimum "
          f"of 7 meals to function! ")
    low_sample_response = input(
        "\nPlease press 'enter' to proceed to add your own meals, "
        "or any other key followed by 'enter' to exit "
        "the program.")
    if low_sample_response == "":
        add_personal_meal()
    else:
        ending_function()


def return_random_meals():
    """
    Return seven randomised meals from the filtered meal list
    and display to user.
    Ask user if they are happy with the selection,
    if not, re-run the function to return a different selection.
    """
    random_meals = random.sample(filtered_meal_list, 7)
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
        "please press 'enter' to continue.\n"
        "If you would like to see a different meal plan, "
        "please press any other key and then 'enter':\n")
    )
    if sample_response == "":
        print("We're glad you like your Evening Meal Plan!\n")
        create_shopping_list(random_meals)

    else:
        return_random_meals()


def create_shopping_list(random_meals):
    """
    Create and display a shopping list based on the ingredients
    required for the meals in the meal plan.
    """
    print("Here is your shopping list for the week:\n")
    shopping_list = []
    for meal in random_meals:
        for ingredient in meal.ingredients:
            shopping_list.append(ingredient)

    for item in sorted(shopping_list):
        print(item.capitalize())

    print("")

    show_recipes(random_meals)


def show_recipes(random_meals):
    """
    Ask user if they would like to see recipe links
    for the meals in their meal plan.
    If yes, display recipe links.
    """
    recipe_response = (input(
        "If you would like to see links to recipes, "
        "please press 'enter'.\n"
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
        print("")
        personal_meals_request()


def personal_meals_request():
    """
    Ask user if they would like to add their own meals
    to the Meal Planner.
    If yes, run Add Personal Meal function.
    """
    personalise_response = input(
        "To customise your experience, "
        "would you like to add your own meals to the Meal Planner?\n"
        "If yes, please press 'enter'.\n"
        "If no, please press any other key and then 'enter' to continue:\n"
    )

    if personalise_response == "":
        add_personal_meal()
    else:
        ending_function()


def add_personal_meal():
    """
    Ask for user input to create a new Meal object
    and add it to the filtered meal list.
    Repeat process if user would like to add another meal,
    otherwise ask if they would like to see a new meal plan
    or exit the program.
    """
    while True:
        new_name = input("Please enter the name of your meal:\n")
        if validate_input(new_name):
            break

    while True:
        contains_input = input(
            "Please enter any ingredients, separated with commas, "
            "that users may dislike or be allergic to:\n"
            )
        # Split and remove trailing whitespace from ingredients input.
        new_contains = [x.strip() for x in contains_input.split(',')]
        if validate_input(contains_input):
            break

    # Skip the validate input function to allow for special characters
    # and numbers in the website url.
    new_recipe = input(
            "Please enter a link to the recipe for your meal:\n"
            )

    while True:
        ingredients_input = input(
            "Please enter the ingredients for your meal, "
            "separated with commas:\n"
        )
        # Split and remove trailing whitespace from ingredients input.
        new_ingredients = [x.strip() for x in ingredients_input.split(',')]
        if validate_input(ingredients_input):
            break

    NewMeal = Meal(
        new_name.title(),
        new_contains,
        new_recipe,
        new_ingredients,
    )
    # Append the new meal item to the filtered meal list.
    filtered_meal_list.append(NewMeal)

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
        # Check if the meal list remains under 7 items,
        # repeat 'sample too low' function if true.
        if len(filtered_meal_list) < 7:
            sample_too_low()
        else:
            print("")
            restart_program_response = input(
                "Would you like to see a new meal plan?\n"
                "If yes, please press 'enter'\n"
                "To exit the program, press any key, followed by 'enter'"
            )

            if restart_program_response == "":
                return_random_meals()
            else:
                ending_function()


def validate_input(user_input):
    """
    Validate user input to all strings and strings with commas
    to prevent errors.
    """
    # Check for empty user input.
    if not user_input:
        print("Input cannot be blank. Please try again.\n")
        return False
    # Check input is only letters, space or commas.
    elif all(char.isalpha() or char.isspace() or char == ','
             for char in user_input):
        return True
    else:
        print("Invalid input. Please use letters, spaces, and commas only.\n")
        return False


def ending_function():
    """
    End program with a thank you message.
    """
    print("")
    print("Thank you for using the Evening Meal Planner\n")


# Initial welcome message.
print("Welcome to your Evening Meal Planner!\n")

# Run start of program with 'get restrictions' function.
get_restrictions()
