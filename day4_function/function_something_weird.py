# def greet_user(name, age = 30, gender = "female"):
#     call_gender = "lady" if gender == "female" else "gentleman"
#     print(f"hello {name.title()}, {age}'s old {call_gender.title()} ")
#
# greet_user("jung")
# greet_user(name = "liu", gender = "soem", age = 20 )

# def make_shirt(size = "large", text = "I love Python"):
#     print(f"size is {size}")
#     print(f"message is {text}")
#
# make_shirt()
# make_shirt(30, "how are you")

def full_name(first, last, middle=None):
    if middle is None:
        print(f"{first} {last}")
    else:
        print(f"{first} {middle} {last}")

full_name("jung", "yu")


def build_person(first, last, age=None):
    person = {'first' : first, 'last' : last}
    if age:
        person['age'] = age
    print(person)


build_person("jung", "yu", "30")




