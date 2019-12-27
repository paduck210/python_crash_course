import math

def isPP(x):
    for i in range(2,x):
        if i ** int(round(math.log(x, i))) == x:
            y = int(round(math.log(x, i)))
            # 3 = int(round(math.log(8, 2)))
            # 2 = int(round(math.log(36, 6)))
            # 2 = int(round(math.log(25, 5)))
            return([i, y])


print(isPP(17))
print(isPP(343))
print(isPP(36))
print(isPP(81))



# isPP(4) => [2,2]
# isPP(8) => [2,3]
# isPP(9) => [3,2]
# isPP(5) => None