from itertools import permutations

def next_smaller(num):
    if len(str(num)) < 2: return(-1)
    else:
        l = list(map(''.join, permutations([i for i in str(num)])))
        l = sorted([int(n) for n in l])
        match_index_number = l.index(num)
        if match_index_number == 0: return(-1)
        else:
            return(l[match_index_number-1])


n = 413
print(next_smaller(n))



