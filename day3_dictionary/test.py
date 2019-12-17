
person = {
    "language": "Python",
    "name": "jung"
}

names = {
    "c_jung": "Python",
    "b_jay": "Java",
    "a_johny": "JS",
    "a_johny": "Python"
}

friends = [ "mimi", "jay", "johny"]

for friend in friends:
    if friend in names.keys():
        print(f"{friend} likes {names[friend]}")
    elif friend not in names.keys():
        print(f"{friend}, you are not my friend")

for name in sorted(names.keys()):
    print(f"{name} = sorted list")


for language in sorted(set((names.values()))):
    print(language)