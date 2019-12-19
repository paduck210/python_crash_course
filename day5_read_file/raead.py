
file_name = 'digit.txt'

with open(file_name) as file:
    lines = file.readlines() #turn to the list
    string = ''
    for line in lines:
        string += line.rstrip()

print(string)
print(len(string))