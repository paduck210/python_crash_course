pizzas = ["peporoni", "cheese", "meat lover"]
friend_pizzas = pizzas[:]

pizzas.append("diavolo")

friend_pizzas.append("vegieterian")


print("my pizza")
for pizza in pizzas:
  print(f"\t{pizza}")


print("friend_pizzas")
for pizza in friend_pizzas:
  print(f"\t{pizza}")

