import math
from functools import reduce

def get_check_list(n):
    lst = [1]
    for num in range(2,n):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            lst.append(num)

    a = 1
    check_lst = [1]
    for num in lst:
        a += num
        check_lst.append(a)
    return(check_lst)


def hamming(origin_num): # n = 13
    if origin_num == 1:
        return 1
    elif origin_num == 2:
        return 2
    elif origin_num == 3:
        return 3
    else:
        a = round(origin_num ** 0.5)
        check_lst = get_check_list(2**a)
        find_num = [i for i in check_lst if i > origin_num]
        index_num = check_lst.index(find_num[0])
        check_num = check_lst[index_num-1]

        three_nums = []
        for a in range(index_num-1):
            for b in range(index_num-1):
                for c in range(index_num-1):
                    if index_num-3 <= (a+b+c) <= index_num:
                        three_nums.append([pow(2,a),pow(3,b),pow(5,c)])

        times_nums = [ reduce(lambda x, y: x*y, three_num) for three_num in three_nums]
        times_nums.sort()
        re_nums = [num for num in times_nums if 2**(index_num-1) <= num ]
        return(re_nums[origin_num-check_num])



print(hamming(100))
