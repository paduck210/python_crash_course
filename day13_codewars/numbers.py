# returns "-6,-3-1,3-5,7-11,14,15,17-20"

def solution(args):
    add_list = []
    for i in args:
        if i-1 in args:
            add_list.append([i])
        else:
            add_list[-1:] += [i]

    add_list.fl
    print(add_list)



solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])

