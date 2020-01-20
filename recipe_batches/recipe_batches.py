#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # For ingredient in the recipe:
    counter = 0
    while True:
        for key in recipe.keys():
            print('recipe count', key, recipe[key])
            # if we need more than we have:
            if key not in ingredients.keys() or recipe[key] > ingredients[key]:
                # return the counter
                break
            # if we have more than we need:
            else:
                print('ingredients count', key, ingredients[key])
                # subtract the needed amount from ingredients
                ingredients[key] -= recipe[key]
    # add one to the counter
        counter += 1
    # repeat the loop
    return counter
    # return the counter


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
