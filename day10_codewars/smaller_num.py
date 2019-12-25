from itertools import permutations

def next_smaller_old(num):
    if len(str(num)) < 2: return(-1)
    else:
        l = list(map(''.join, permutations([i for i in str(num)])))
        l = sorted([int(n) for n in l])
        match_index_number = l.index(num)
        if match_index_number == 0: return(-1)
        else:
            return(l[match_index_number-1])

# 531
# 513
# 351
# 315
# 153
# 135
# >> 4312
# len(4321) = 4
# 0 , 1 , 2,


def next_smaller(num):
    if num < 20: return(-1)
    else:
        index = len(str(num)) #3
        for i in range(index): # 0,1,2
            int(num)[i-index] > int(num)[i-]




        int(num[-3]) > int(num[-2])
        int(num[-2]) > int(num[-1])







n = 413
print(next_smaller(n))



