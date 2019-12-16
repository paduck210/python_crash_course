user_names = ["jung", "paduck", "admin", "may", "bay"]
# user_names = []

if user_names:
    for user_name in user_names:
        # if user_name is "admin":
        #     print(f"Hello {user_name}, time to work")
        # else:
        #     print(f"How are you {user_name}")
        print(f"{user_name}, time to work") if user_name is "admin" else print(f"{user_name}, how r u")
else:
    print("list is empty")



#
# b = 2 if a is 2 else None
#
# if a is 1:
#     b = 2
# else:
#     b = None
