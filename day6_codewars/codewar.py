# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51


def dig_pow(n, p):
    check_sum = sum(int(num) ** (p + i) for i, num in enumerate(str(n)))
    return check_sum // n if check_sum % n == 0 else -1

def dig_pow(n,p):
    check_sum = sum(int(num) ** (p + i) for i, num in enumerate(len(str(n))))
    return check_sum // n if check_sum % n == 0 else -1



    #
    # for i in range(len(str(n))):
    #     number = str(n)[i]
    #     numbers.append(int(number)**p)
    #     p += 1
    # if sum(numbers) % n == 0:
    #     return sum(numbers)//n
    # else:
    #     return -1

print(dig_pow(92,1))
print(dig_pow(695,2))
print(dig_pow(46288,3))
