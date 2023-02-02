# Pete likes to bake some cakes. He has some recipes and ingredients.
# Unfortunately he is not good in maths. Can you help him to find out,
# how many cakes he could bake considering his recipes?

# Write a function cakes(), which takes the recipe (object) and the available
# ingredients (also an object) and returns the maximum number of cakes Pete can
# bake (integer). For simplicity there are no units for the amounts
# (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
# Ingredients that are not present in the objects, can be considered as 0.

# Examples:

# # must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# # must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})


import math
import os

# Clearing the Screen
os.system('cls')


def cakes(recipe, available):
    itemRecipe = list(recipe.keys())
    itemAvaileable = list(available.keys())
    boolList = [True if item in itemAvaileable else False for item in itemRecipe]
    if not all(boolList):
        return 0
    else:
        minList = {}
        aux = math.inf
        for item in itemRecipe:
            minList[item] = math.floor(available[item]/recipe[item])
            if minList[item] < aux:
                limit = item
                aux = minList[item]

    return minList[limit]


recipe = {
    "flour": 500,
    "sugar": 200,
    "eggs": 1
}

available = {
    "eggs": 5,
    "sugar": 1200,
    "milk": 200,
    "flour": 1200,
}

x = cakes(recipe, available)
print(x)


# ! BESTO RESPUESTA
def cakes2(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)
