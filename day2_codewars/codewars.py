
# words = list(s.split(" "))
# key = words[0]
# for word in words:
#   if len(word) < len(key):
#     key = word
# print(key)





return min(len(x) for x in s.split())

string = "I love you"
print(string.split())
print([x for x in string.split(" ")])
print([len(x) for x in string.split(" ")])
print(min([len(x) for x in string.split(" ")]))



string_2 = "I love you 2"
print(string_2.split())
print([x for x in string_2.split(" ")])


a = 1
def doSeomthing():
  a = 2


doSeomthing()
print(a)
