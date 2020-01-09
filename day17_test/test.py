string = "Hello world"

def reverse(str):
    lst = list(str)
    new = []
    while lst != []:
        new.append(lst.pop())
    return(''.join(new))


    # str_list = [lst[-i] for i in range(1,len(lst)+1)]
    # str = ''.join(str_list)
    # return(str)

print(reverse(string))


