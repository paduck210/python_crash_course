from itertools import product
from functools import reduce

def hamming(n):
    two = [pow(2, num) for num in range(n)]
    three = [pow(3, num) for num in range(n)]
    five = [pow(5, num) for num in range(n)]
    new = product(two, three, five) #[(1, 1, 1), (1, 1, 5), (1, 3, 1), (1, 3, 5), (2, 1, 1), (2, 1, 5), (2, 3, 1), (2, 3, 5)]
    three_nums = [[num for num in lst] for lst in new]
    times_nums = []
    for three_num in three_nums:
        times_nums.append(reduce(lambda x, y: x*y, three_num))
    times_nums.sort()
    return(times_nums[n-1])

print(hamming(17))
print(hamming(19))

# time out...!!!