# returns "-6,-3-1,3-5,7-11,14,15,17-20"

def solution(args):
    add_list = []
    for i in args:
        if i-1 in args:
            n = add_list.pop() + [i]
            add_list.append(n)
        else:
            add_list.append([i])

    print(add_list)

    string = ""
    for l in add_list:
        if len(l) == 1:
            string += f"{l[0]},"
        elif len(l) == 2:
            string += f"{l[0]},{l[-1]},"
        else:
            string += f"{l[0]}-{l[-1]},"
    return(string[0:-1])



print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

