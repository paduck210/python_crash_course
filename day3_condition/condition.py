foods = ["sushi", "pasta", "bagle"]
new_fruit = "melon"

print(new_fruit in foods)
if new_fruit not in foods:
    foods.append((new_fruit))
    print(f"{new_fruit} is added on list")

print(foods)
