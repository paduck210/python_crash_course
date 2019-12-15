food = ["pasta", "pizza", "bibimbap", "Pazun"]
print(food)



# Add on the list

# append
new_food = "fired rice"
food.append(new_food)
print(food)

# insert
food.insert(1,"smoke meat")
print(food)


# Delete element
# pop removes the item at a specific index and returns it.
name = ["harry", "Potter", "emma", "marry"]
print(name.pop()) # marry
print(f"I just removed the name : {name.pop(2)}") # emma
print(name) # ['harry', 'Potter']


# del removes the item at a specific index:
name = ["harry", "Potter", "emma", "marry"]
del name[0]
print(name) # ['Potter', 'emma', 'marry']



# sort : change original data
food = ["pasta", "pizza", "bibimbap", "Xianmi"]
food.sort()
print(food)

# sorted : maintain original order of a list
food = ["pasta", "pizza", "bibimbap", "Xianmi"]
print(sorted(food))


# reverse
food = ["pasta", "pizza", "bibimbap", "Xianmi"]
print(food)
food.reverse()
print(food) # ['Xianmi', 'bibimbap', 'pizza', 'pasta']


print(len(food)) #4



# print(food[3][0].isupper())
# print(food[3][1].isupper())
print("HELLO")
