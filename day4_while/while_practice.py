prompt = "Enter something: "

message = ""

while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)



current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)



