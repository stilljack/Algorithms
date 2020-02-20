#!/usr/bin/python

import math

def recipe_batches(recipe:dict, ingredients:dict):
  #if mismatch of keys, return false
  totalCount=[]
  if recipe.keys()!=ingredients.keys():
    return -0
  for k,v in ingredients.items():
    print(f"recipe v{recipe[k]} ingre v {v}")
    #check how many we can make, i.e the value divided by how much we need for one recipe
    res=v//recipe[k]
    #appen to totalcount
    totalCount.append(res)

    ##csort should be fine
  totalCount.sort()
    #hey _Minimum loops in the function itself... sorting doesn't count right? hahaha
  return totalCount[0]



# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
