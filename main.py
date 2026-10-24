pasta = ("Pasta Arribata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")
print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])

all_recipes = (pasta, biryani)
print("\nFirst Recipe Name:", all_recipes[0][0])
print("Second Recipe Name:", all_recipes[1][2])
print("Pasta details(Sliced):", pasta[1:3])

print("\nPasta Recipie Details:")
for detail in pasta:
    print("- ", detail)

pasta_ingredients = ["tomato", "garlic", "olive oil", "chili", "pasta"]
biryani_ingredients = ["chicken", "rice", "spices", "galic", "onion", "tomato"]
print("\nPasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)
print("Total Pasta Ingredients:", len(pasta_ingredients))

pasta_ingredients.append("parmesan")
pasta_ingredients.remove("chili")
print("\nUpdated Pasta Ingredients:", pasta_ingredients)

all_ingredients = set(pasta_ingredients).union(set(biryani_ingredients))
common = set(pasta_ingredients).intersection(set(biryani_ingredients))
only_pasta = set(pasta_ingredients).difference(set(biryani_ingredients))
unique_to_each = set(pasta_ingredients).symmetric_difference(set(biryani_ingredients))

print("\nAll Ingredients:", all_ingredients)
print("Common Ingredients:", common)
print("Only in Pasta(Difference):", only_pasta)
print("Not Shared:", unique_to_each)