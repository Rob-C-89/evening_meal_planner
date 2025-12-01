

# Evening Meal Planner

Evening Meal Planner is a Python terminal application, which runs in the Code Institute mock terminal on Heroku.

It is a program designed to return to the user a random meal plan of seven meals, one for each day of the week. Evening Meal Planner is interactive with the user, allowing them to manipulate the data structure with certain features.

The completed program can be viewed [here](https://evening-meal-planner-9fed6f279af0.herokuapp.com/).

# Table of Contents

- User Stories
- Project Planning
- Features
- Testing
- Deployment
- Credits

## User Stories

User stories for the program include:

 - I am a person looking for a program to automatically generate a daily
   evening meal plan for the week.

-   I want the meal planner to adapt to my specific allergies or
   dislikes.
  
-   I want to have access to recipes for the meals to help me follow the
   meal plan.
   
-   I want to have a shopping list created for the plan.
   
-   I want the option to add my own bespoke meals to the list of meals.

## Project Planning

The user stories for the program and their acceptance criteria are outlined in the GitHub projects planning page which can be found [here](https://github.com/users/Rob-C-89/projects/9).

### Flowchart

A flowchart outlining the user journey has been created using [Lucidchart](https://www.lucidchart.com/pages/).

![Flowchart image of program structure](assets/documentation/emp_flowchart.png)

## Features

### Key Features

**Preliminary dietary restrictions**

Before returning their weekly meal plan, the user is asked if they have any allergies or dislikes. This compiles a list of dietary restrictions. The meal list is then filtered, to prevent dishes containing these foods from being returned to the user.

**Random meal plan generation**

The program then provides the user with a randomly generated list of seven meals, one for each day of the week. The user is asked if they are happy with their selection, or if they would like to see a different list.

**Shopping list creation**

After accepting their meal plan, the user is provided with a shopping list. This contains all the ingredients listed in the meals for their plan.

**Links to recipes**

The user is then asked if they would like to see recipe links for their meals.

**Add customised personal meals**

The user has the option to create their own meals and add them to the data structure. They can add as many meals as they like. They then have the option to generate another meal list, which may include the meals they have added, or exit the program.

### Future Features

The scope for extra features in this program is considerable. I ended the project having surpassed my standards for a minimum viable product, but some potential future features may include:


1. Separation of the contains/restrictions and the ingredients attributes. At conception of the project, the contains/restrictions attributes for the meal items was to be the only data used to filter the meals list, whereas the ingredient attributes was designed for the purpose of the shopping list.

   As the project progressed, it made sense to include the ingredients when filtering for disliked ingredients. 

   In the future, I would re-write the restrictions function to be a dropdown/numbered list of the 14 common allergens, and then have a seperate information request for dislikes. This would prevent someone who is allergic to fish, and mistyping e.g. 'fihs', being returned a list containing 'fish'.

2. The option to target and remove specific meals on the returned meal plan - if out of the seven meals, the user disliked the idea of one meal, they could have it removed and keep the meal plan mostly the same, with a new random meal for the removed item.

3. A main menu, with a differently organised flow to the program. As I progressed in my project, the flow of the user interactions grew slightly more complex than I had initially anticipated. 
   I consider it to still be a user-friendly and intuitive program, but with more time I would have the user land on a 'main menu', with options to begin with either seeing a meal plan, viewing the meal database, adding restrictions, or adding their personal meals. This would let the user tailor the experience more to their specific requirements.

4. Using an external database i.e. google sheets for the database. 

5.  Quantities for the shopping list i.e. 500g fish, 200g potatoes, etc.
    
6.  User input for the number of people following the meal plan, and this manipulating the shopping list quantities.
    
7.  A user login which saves restrictions and customised meals for future use.
    
8.  The option for the user to choose their own meal plan from the data centre, rather than see a random selection.

### Input Validation

1. When entering their restrictions, the user is prevented from responding with anything other than letters, whitespace and commas. The user can also not enter nothing and press enter. This is to prevent incorrect data input, and to encourage the user to write in the correct format to generate lists of items.

2. If the user's restrictions take the filtered meal list to below 7 items, they are requested to add their own meals, until the list has a minimum of 7 items.

3. On adding personal meals, the user is again prevented from entering anything other than letters, whitespace and commas, or inputting empty data, for the name, contains and recipe attributes. The same validation is not used for the recipe link, as this may contain numbers and symbols.

    
## Testing

## Deployment

## Credits