import random

# create 100 Monsters
monsters = []
colors = ["red", "green", "orange", "black", "blue"]

for monster in range(100):
    new_monster = {'color': random.choice(colors), 'points': random.randrange(1,10)}
    monsters.append((new_monster))

# check the number of color monsters got
color_list = {}
for color in colors:
    color_list[color] = 0
    for monster in monsters:
        if monster['color'] == color:
            color_list[color] += 1


if len(monster) == sum(color_list.values()):
    print("warning")
else:
    for k, v in color_list.items(): #sorted by Value
        print(f"\t{k.title()} = {v}")
    print(f"Total: {sum(color_list.values())} ")


