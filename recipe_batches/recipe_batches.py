#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # set batch count to inf
    batches = float('inf')
    # for key in recipe dict keys:
    for key in recipe.keys():
        # if the key is in the ingredients dict and the value is not higher than in ingredients:
        if key in ingredients.keys() and ingredients[key] >= recipe[key]:
            # floor divide ingredients value by recipe value
            temp = ingredients[key] // recipe[key]
            # if its smaller than batch count, replace batch count
            if temp < batches:
                batches = temp
        else:
            batches = 0
            break
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
