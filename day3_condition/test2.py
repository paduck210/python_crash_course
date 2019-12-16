current_users = ["jung", "paduck", "admin", "may", "bay"]
new_users = ["Jung", "paduck", "mimi", "pam", "john"]

for user in new_users:
    print(f"{user} is already taken") if user.lower() in current_users else print(f"you can user {user}")
