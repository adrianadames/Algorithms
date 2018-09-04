#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
  recipe1 = []
  ingredients1=[]
  bottleneck = []

  for i, value in recipe.items():
      recipe1.append(value)
  print(recipe1)
  for i, value in ingredients.items():
      ingredients1.append(value)
  print(ingredients1)
  for i in range(len(ingredients)):
    bottleneck.append(math.floor(ingredients1[i]/recipe1[i]))
  print(bottleneck)
  for i in range(len(bottleneck)):
    if bottleneck[i]<bottleneck[i-1]:
      numberOfBatches = bottleneck[i]
  if numberOfBatches == 0:
    print('No batches can be made given these ingredients')
  else:
    print(f'{numberOfBatches} batches can be made given these ingredients')
    

    



recipe = { 'milk': 100, 'butter': 50, 'flour': 52 }
ingredients = { 'milk': 382, 'butter': 148, 'flour': 51 }

recipe_batches(recipe, ingredients)

# for i in range(len(recipe))
# print(recipe1, ingredients1)





# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))